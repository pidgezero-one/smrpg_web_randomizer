from markdown import markdown
from enum import StrEnum
from typing import Generic, TypeVar
from ..data.spells.spells import ALL_SPELLS
from ..types.spell import CharacterSpell
from ..data.allies.allies import ally_collection
from ..progression.prizes import ALL_BOSS_FIGHTS, BossFightPrize
from .base import CategorizationOption, ClassCategorizationOption
from copy import deepcopy


class FlagError(ValueError):
    pass


class FlagType(StrEnum):
    BOOLEAN = "boolean"
    CATEGORIZATION = "categorization"
    CATEGORIZATION_WITH_ORDINANCE = "categorization_with_ordinance"
    RANGE = "range"
    SELECT_ONE = "select_one"


class Flag:
    """Class representing a flag with its description, and possible values/choices/options."""

    _name = ""
    _description = ""
    _default = None
    _id = ""
    _requires_all = []
    _requires_any = []
    type: FlagType

    @property
    def description(self):
        return markdown(self._description)

    @property
    def description_or_name(self):
        if self._description:
            return self.description
        else:
            return markdown(self._name)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id


# TypeVars for generic flag classes
from enum import Enum
T = TypeVar("T", bound=Enum)


class CategorizationFlag(Flag, Generic[T]):
    """For things like selecting which locations can and cannot contain progression"""

    type = FlagType.CATEGORIZATION
    _options: dict[T, bool] = {}
    _default: dict[T, bool] = {}

    @property
    def enabled(self) -> list[T]:
        return [option for option, enabled in self.options.items() if enabled]

    @property
    def disabled(self) -> list[T]:
        return [option for option, enabled in self.options.items() if not enabled]

    def enable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        self.options[option] = True

    def disable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        self.options[option] = False

    @property
    def default(self) -> dict[T, bool]:
        return self._default

    @property
    def options(self) -> dict[T, bool]:
        return self._options or self.default.copy()

    def reset(self) -> None:
        self._options = self.default.copy()

    def __init__(self, options: dict[T, bool] | None = None) -> None:
        if options is not None:
            for option, enabled in options.items():
                if enabled:
                    self.enable(option)
                else:
                    self.disable(option)
        else:
            self._options = self.default.copy()


class CategorizationFlagWithOrdinance(Flag, Generic[T]):
    """For thing like choosing your starting party where order matters"""

    type = FlagType.CATEGORIZATION_WITH_ORDINANCE
    _options: dict[T, int | None] = {}
    _default: dict[T, int | None] = {}

    @property
    def default(self) -> dict[T, int | None]:
        return self._default

    @property
    def options(self) -> dict[T, int | None]:
        return self._options or self.default.copy()

    @property
    def enabled(self) -> list[T]:
        return sorted(
            [option for option, enabled in self.options.items() if enabled is not None],
            key=lambda x: (
                self.options[x] is None,
                self.options[x] if self.options[x] is not None else 0,
            ),
        )

    @property
    def disabled(self) -> list[T]:
        return [option for option, enabled in self.options.items() if enabled is None]

    def enable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        max_value = max((v for v in self.options.values() if v is not None), default=-1)
        self.options[option] = max_value + 1

    def disable(self, option: T) -> None:
        if option not in self.options:
            raise FlagError(f"Option {option} is not a valid option for this flag.")
        previous_value = self.options[option]
        self.options[option] = None
        if previous_value is not None:
            for opt, val in self.options.items():
                if val is not None and val > previous_value:
                    self.options[opt] = val - 1

    def reset(self) -> None:
        self._options = self.default.copy()

    def __init__(self, options: dict[T, int | None] | None = None) -> None:
        self._options = self.default.copy()
        if options is not None:
            for k in options.keys():
                assert k in self._options
            self._options = deepcopy(options)


class SelectOneFlag(Flag, Generic[T]):
    """For things like choosing an area gating option can and cannot contain progression"""

    type = FlagType.SELECT_ONE
    choices: list[T] = []
    _selected: T
    _default: T

    @property
    def selected(self) -> T:
        return self._selected or self._default

    def select(self, choice: T) -> None:
        if choice not in self.choices:
            raise FlagError(f"Choice {choice} is not a valid option for this flag.")
        self._selected = choice

    @property
    def default(self) -> T:
        return self._default

    def reset(self) -> None:
        self._selected = self.default

    def __init__(self, choice: T | None = None) -> None:
        if choice is not None:
            self.select(choice)
        else:
            self.select(self.default)


class BooleanFlag(Flag):
    """For simple true/false flags"""

    type = FlagType.BOOLEAN
    enabled: bool = False
    _default: bool = False

    @property
    def default(self) -> bool:
        return self._default

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def reset(self):
        self.enabled = self.default

    def __init__(self, enabled: bool | None = None) -> None:
        if enabled is not None:
            self.enabled = enabled
        else:
            self.enabled = self.default


class RangeFlag(Flag):
    """For flags that have a range of integer values"""

    type = FlagType.RANGE
    min_value: int = 0
    max_value: int = 100
    _value: int = 0
    _default: int = 0

    @property
    def default(self) -> int:
        return self._default

    @property
    def value(self) -> int:
        return self._value or self.default

    def set_value(self, value: int):
        if value < self.min_value or value > self.max_value:
            raise FlagError(f"Value {value} is out of range for this flag.")
        self._value = value

    def reset(self):
        self._value = self.default

    def __init__(self, threshold: int | None = None) -> None:
        if threshold is not None:
            self.set_value(threshold)
        else:
            self.set_value(self.default)


# ✅ = implemented


# ******** Party


class ShuffleCharacters(BooleanFlag):
    _name = "Randomize party recruitment order"
    _description = """If enabled, your characters will join your party in a random order.
<br>
<br>If disabled, you will start with Mario and recruit characters near their original locations."""
    _id = "random"


class MaxCharacters(RangeFlag):
    _name = "Number of characters available"
    _description = "The total number of playable characters. Set this to 1 if you are attempting a solo challenge."
    min_value = 1
    max_value = 5
    _default = 5
    _id = "max"


class StartingCharacterEnum(ClassCategorizationOption):
    pass


for ally in ally_collection._allies:
    attr_name = ally.name.replace(" ", "_").replace("-", "_")
    setattr(StartingCharacterEnum, attr_name, type(ally))


class StartingCharacters(CategorizationFlagWithOrdinance[StartingCharacterEnum]):
    _name = "Starting Characters"
    _default: dict[StartingCharacterEnum, int | None] = {
        o: True
        for i, o in enumerate(StartingCharacterEnum.__members__.values())
        if i == 0
    }
    _description = "The characters who will be in your party at the start of the game. Your first selection will be considered your starting character."
    _id = "starters"


class PlayAsStarter(BooleanFlag):
    _name = "Play as starting character everywhere"
    _description = """If enabled, the character on your file select menu (also the character in your default 1st party position) will also be the character you play as outside of battle.
<br>
<br>If disabled, you will always play as Mario outside of battle, regardless of whether or not he is in your party."""
    _id = "protag"


# ******** Equipment


# ✅
class EquipmentCharactersOptions(CategorizationOption):
    """Enumeration for character equipment guidelines"""

    VANILLA = "Vanilla"
    VANILLA_ACCESSORIES_ALL = "Vanilla, except anyone can wear any accessory"
    RANDOM_ACCESSORIES_ALL = "Random, except anyone can wear any accessory"
    RANDOM = "Completely random"
    EQUIP_ALL = "Anyone can equip anything"


# ✅
class EquipmentCharacters(SelectOneFlag[EquipmentCharactersOptions]):
    _name = "Equipment permissions"
    _description = """<b>Vanilla</b>: The list of characters who are permitted to equip each item remains unchanged from the original game.
<br>
<br><b>Vanilla, except anyone can wear any accessory</b>: Armor and weapon permissions are unchanged from the original game, but all accessories can be equipped by anyone.
<br>
<br><b>Random, except anyone can wear any accessory</b>: Armor and weapon permissions are randomized, but all accessories can be equipped by anyone.
<br>
<br><b>Completely random</b>: All equips' permissions are randomized.
<br>
<br><b>Anyone can equip anything</b>: No equips are character-restricted."""
    choices = [o for o in EquipmentCharactersOptions]
    _default = EquipmentCharactersOptions.VANILLA
    _id = "perms"


# ✅
class EquipmentPropertiesOptions(CategorizationOption):
    VANILLA = "Vanilla"
    SOME = "Some buffs added"
    RANDOM = "Completely random"


# ✅
class EquipmentProperties(SelectOneFlag[EquipmentPropertiesOptions]):
    _name = "Equipment stats & buffs"
    _description = """<b>Vanillat</b>: The stats and buffs on equipment are unchanged from the original game.
<br>
<br><b>Some buffs added</b>: The stats and buffs on equipment are mostly unchanged from the original game, except most armors are given one additional property (e.g. Fire Shirt nullifies damage from fire attacks). Additionally, some weapons will boost magic attack instead of physical attack.
<br>
<br><b>Completely random</b>: The stats and buffs on each piece of equipment is randomized."""
    choices = [o for o in EquipmentPropertiesOptions]
    _default = EquipmentPropertiesOptions.VANILLA
    _id = "props"


# ✅
class IgnoreNamesakeProperties(BooleanFlag):
    _name = "No equipment property guarantees"
    _description = "Normally, certain namesake items retain their protections: <b>Fearless Pin</b>, <b>Antidote Pin</b>, <b>Trueform Pin</b>, and <b>Wakeup Pin</b>. In addition, at least four equips will have OHKO protection. This flag removes those guarantees."
    _id = "unsafe"


# ✅
class StarPieceHints(BooleanFlag):
    _name = "Signal Ring Star Piece hints"
    _description = """If enabled, the Signal Ring (if equipped to your active party) will play a sound when you enter a world area that contains a Star Piece.  
<br>
<br>The Signal Ring will only sound off when you enter an area from the World Map, from loading a save, or from an area warp (ex: the Kero Sewers - Land's End pipe). Therefore, the chime does not necessarily indicate that your current room contains a Star Piece, but rather that at least one room in the area does."""
    _id = "hints"


# ******** Stats & Spells


# ✅
class EXPMultiplierOptions(CategorizationOption):
    """Enumeration for EXP scaling from enemy battles"""

    VANILLA = "Default"
    DOUBLE = "Double"
    TRIPLE = "Triple"


# ✅
class EXPMultiplier(SelectOneFlag[EXPMultiplierOptions]):
    _name = "EXP multiplier"
    _description = (
        """If not set to "Default", all EXP gained will be doubled or tripled."""
    )
    choices = [o for o in EXPMultiplierOptions]
    _default = EXPMultiplierOptions.VANILLA
    _id = "exp"


# ✅
class CharacterStats(BooleanFlag):
    _name = "Randomize character stats"
    _description = """If enabled, stats and stat curves for each playable character will be randomized. This also randomizes the number of FP you start with.
<br>
<br>If disabled, playable characters retain their original stats and stat curves."""
    _id = "stats"


class CharacterLearnedSpells(BooleanFlag):
    _name = "Randomize character learned spells"
    _description = "The pool of spells learnable by each character will be randomized. This only covers spells originally learn-able by playable characters, and does not include enemy spells."
    _id = "spells"


# ✅
class CharacterSpellStats(BooleanFlag):
    _name = "Randomize character spell stats"
    _description = "The power and FP cost of character magic spells will be randomized."
    _id = "spellstats"


# ✅
class InfuseSpellElements(BooleanFlag):
    _name = "Infuse more spells with elements"
    _description = "Geno Beam becomes an ice spell, Geno Flash and Psych Bomb become fire spells, and Crusher and Bowser Crush become earth (jump) spells."
    _id = "infuse"


# ✅
class CharacterSpellElements(BooleanFlag):
    _name = "Randomize character spell elements"
    _description = "Character spells with elements will have their elements randomized. Non-elemental spells will remain non-elemental."
    _id = "spellelements"


# ✅
class UncapSuperJumps(BooleanFlag):
    _name = "Uncap Super Jumps"
    _description = "If enabled, you can do more than 100 Super Jumps at once."
    _id = "uncap"


class LearnableSpellEnum(ClassCategorizationOption):
    """Enumeration for all learnable spells"""

    pass


# Populate the LearnableSpellEnum with spell classes
for spell in ALL_SPELLS.spells:
    if isinstance(spell, CharacterSpell):
        attr_name = spell.title.replace(" ", "_").replace("-", "_")
        setattr(LearnableSpellEnum, attr_name, type(spell))


class AvailableSpells(CategorizationFlag[LearnableSpellEnum]):
    _name = "Available Player Spells"
    _description = """Highlighted (white text over blue) spells will be learned by at least one character. Spells that are not highlighted will not be learned by any character.
<br>
<br>Excluded spells are not replaced in characters' learnsets by other spells, so some characters will learn less than six total.
<br>
<br>Note: You need at least one damage spell available to transform Mokura. Spells required for checks (i.e. super jump) cannot be excluded."""
    _default = {o: True for o in LearnableSpellEnum.__members__.values()}
    _id = "avail"


# ******** Star Pieces and Bosses


# if this is disabled, no other options in this category can be changed
class ShuffleStarPieces(BooleanFlag):
    _name = "Randomize the locations of Star Pieces"
    _description = """If enabled, the Star Pieces may be found in places other than their original locations.
<br>
<br>If disabled, they will be rewarded by defeating the final bosses of Mushroom Kindom, Forest Maze, Moleville, Seaside Town, and Barrel Volcano, as well as a freestanding piece on Star Hill."""
    _id = "random"


class TotalStarPieces(RangeFlag):
    _name = "Total Star Pieces available"
    _description = (
        "The total number of Star Pieces (0-7) that can be collected in the seed."
    )
    _default = 6
    min_value = 0
    max_value = 7
    _id = "avail"


# EnabledBossChecks and EnabledStarPieceChecks are defined after delayed imports below


# ✅
class ProgressionLogicDifficultyOptions(CategorizationOption):
    """Enumeration for progression logic difficulty levels"""

    NORMAL = "Default"
    HARD = "Hard"


# ✅
class ProgressionLogicDifficulty(SelectOneFlag[ProgressionLogicDifficultyOptions]):
    _name = "Progression logic difficulty"
    _description = """<b>Normal</b> - The shuffler will take boss difficulty into account when placing progression items. Your expected early progression items are most likely to be found earlier in the game.
<br>
<br><b>Hard</b> - The shuffler will not consider boss difficulty when placing progression items. Your progression items may be found late in the game among higher level boss battles."""
    _id = "restrict_map"


# ✅
class DisperseStarPieces(BooleanFlag):
    _name = "Disperse Star Pieces evenly across the map"
    _description = """If enabled, each of the seven overworld map areas may only contain up to one Star Piece each.
<br>
<br>Note: This may not be respected if Bowser's Keep and Factory are both gated by 6 Star Pieces."""
    _id = "restrict_map"


# ******** Item shuffle


# if this is disabled, no options in this category can be changed
class ShuffleItems(BooleanFlag):
    _name = "Randomize item rewards"
    _description = """If enabled, the contents of treasure chests, quest rewards, and freestanding small items will be shuffled.
<br>
<br>If disabled, chests, quest rewards, and freestanding small items will remain unchanged from the original game."""
    _id = "random"


class ItemQualityOptions(CategorizationOption):
    """Enumeration for item quality options"""

    ORIGINAL_POOL = "Original item pool"
    COMPLETELY_RANDOM = "Completely random items"
    MOSTLY_RANDOM = "Random items, biased toward low-impact items"
    COMPLETELY_EMPTY = "Completely empty except for progress items"


class ItemQuality(SelectOneFlag[ItemQualityOptions]):
    _name = """Item pool quality"""
    _description = """Determines how non-required items are distributed."""
    choices = [o for o in ItemQualityOptions]
    _default = ItemQualityOptions.ORIGINAL_POOL
    _id = "quality"


class BiasItemShuffle(BooleanFlag):
    _name = "Bias better items to gated locations"
    _description = (
        """If enabled, harder-to-reach areas will generally house better items."""
    )
    _id = "bias"


class NoStarEgg(BooleanFlag):
    _name = "No Star Egg"
    _description = """If enabled, you are guaranteed not to find the Star Egg via any chests, overworld items, NPC rewards, or shops."""
    _id = "noegg"


class RestrictSpecialEquips(BooleanFlag):
    _name = 'Shuffle "Special Item" exchange equips & Monstro Town reward equips'
    _description = """If enabled, the FroggieStick, Chomp, Zoom Shoes, Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost Medal, and both Lazy Shells will be shuffled within each other's original locations, and will not be accessible anywhere else, regardless of your chosen Item Pool Quality setting.
<br>
<br>If disabled, the ten locations will simply contain random items, like every other item location."""
    _id = "restrict_monstro"


class EXPStarsAnywhere(BooleanFlag):
    _name = "Shuffle EXP stars"
    _description = """If enabled, EXP stars may appear in chests that don't house them in the original game.
<br>
<br>If disabled, EXP stars will be restricted to their original locations in Bandit's Way, Kero Sewers, Moleville Mines, Sea, Land's End, Nimbus Land, and Barrel Volcano."""
    _id = "xpstars"


class MimicsAnywhere(BooleanFlag):
    _name = "Shuffle mimic chests"
    _description = """If enabled, any three chests in the world may be mimics. You will be able to run away from them.
<br>
<br>If disabled, mimic chests will remain in their original locations in Kero Sewers, Sunken Ship, and Bean Valley. You will not be able to run away from these fights."""
    _modes = ["open"]
    _id = "mimics"


class SlotsAnywhere(BooleanFlag):
    _name = "Shuffle slot machine chests"
    _description = """If enabled, the three slot machine chests in Bean Valley may be moved elsewhere.
<br>
<br>If disabled, the three original slot machines in Bean Valley will be unchanged."""
    _id = "slots"


class ShuffleBeetlemania(BooleanFlag):
    _name = "Shuffle Beetlemania"
    _description = """If enabled, the Mushroom Kingdom inn kid will give you a random item check for 500 coins. Beetlemania will appear in a random location, unless your item pool is set to "Completely Empty"."""
    _id = "beetle"


class ShuffleMagikoopaChest(BooleanFlag):
    _name = "Shuffle Magikoopa's coin chest"
    _description = """If enabled, the chest in Magikoopa's room will contain a random item check. A random chest somewhere in the game will contain infinite coins, unless your item pool is set to "Completely Empty"."""
    _id = "kamek"


# ✅
class ShuffleWeddingGear(BooleanFlag):
    _name = "Shuffle Marrymore wedding gear"
    _description = """If enabled, the four pieces of wedding gear required to initiate the Marrymore boss fight will be located randomly within the world (not necessarily key item locations). Interacting with the four NPCs in the chapel will become random item checks.
<br>
<br>If disabled, the Marrymore chapel minigame will behave as normal."""
    _id = "marry"


class AnnoyingChests(BooleanFlag):
    _name = 'Empty chests should perform the "You Missed" animation'
    _description = """If disabled, empty chests will simply appear as pre-opened."""
    _id = "ym"


class FireworksOptions(CategorizationOption):
    """Enumeration for Fireworks flag option"""

    VANILLA = "Vanilla"
    SHUFFLE_ONE = "Shuffle Fireworks"
    PROGRESSIVE = "Shuffle Progressive Fireworks"


class FireworksSetting(SelectOneFlag[FireworksOptions]):
    _name = """Fireworks trade sequence"""
    _description = """<b>Vanilla</b>: Unchanged from the original game.
<br>
<br><b>Shuffle Fireworks</b>: Fireworks is added to the "Special Item" pool, and the Fireworks shop becomes a "Special Item" location. The trading sequence is otherwise unchanged. If needed, you may get your Shiny Stone back from the shop girl after you have completed the trade sequence.
<br>
<br><b>Shuffle Progressive Fireworks</b>: One Fireworks, Shiny Stone, and Carbo Cookie are each shuffled somewhere completely random in the game, and you will always receive them in order. The fireworks shop, Pur-Tend store, and cookie girl become item checks. The Monstro Town sealed door is unlocked when you find the Shiny Stone.
<br>
<br>Note: If you do not have Bucket Warp enabled, completing the Carbo Cookie trade sequence will give you a random item if "Shuffle Fireworks" or "Shuffle Progressive Fireworks" is selected.
"""
    choices = [o for o in FireworksOptions]
    _default = FireworksOptions.VANILLA
    _id = "fireworks"


# ******** Progression availability


class KeyItemsAnywhere(BooleanFlag):
    _name = '"Special Items" can appear in the general item pool'
    _description = """If enabled, items belonging to your "Special Items" pocket can appear in any item location.
<br>
<br>If disabled, the "Special Items" will only be shuffled within each other's locations.
<br>
<br>The items targeted by this setting are the <b>Rare Frog Coin</b>, <b>Cricket Pie</b>, <b>Bambino Bomb</b>, <b>Castle Key 1</b>, <b>Castle Key 2</b>, <b>Alto Card</b>, <b>Tenor Card</b>, <b>Soprano Card</b>, <b>Greaper Flag</b>, <b>Dry Bones Flag</b>, <b>Big Boo Flag</b>, <b>Shed Key</b>, <b>Elder Key</b>, <b>Cricket Jam</b>, <b>Temple Key</b>, <b>Room Key</b>, <b>Seed</b>, <b>Fertilizer</b> (and sometimes <b>Bright Card</b> and <b>Fireworks</b>)."""
    _id = "keys_anywhere"
    # change EVENT_947_jmp_to_event_107" to point to event 949


class StarPieceAvailability(BooleanFlag):
    _name = "Star Pieces can appear in the general item pool"
    _description = "If enabled, some Star Pieces may be shuffled in with items instead of being only granted by boss fights."
    _id = "stars_anywhere"
    # change EVENT_947_jmp_to_event_107" to point to event 949


# ✅
class InvisibleFlagsSetting(BooleanFlag):
    _name = "Move invisible flag checks"
    _description = """Chooses where the invisible items placed by the Three Musty Fears are located.
<br>This setting will put your attention to detail and your knowledge of the world of SMRPG to the test.
<br>
<br>If "Default locations" is selected, these checks will remain in their default locations (Mario's Pad bed, Rose Town sign, Yo'ster Isle goalpost).
<br>
<br>If enabled, the three checks will be located somewhere random in the world as an invisible item. The Three Musty Fears will give you hints as to their locations."""
    _id = "moveflags"


class Remake(BooleanFlag):
    _name = "Enable Remake content"
    _description = """If enabled, the seven postgame boss fights from the 2023 Switch remake and their rewards will be available in the game and included in all shuffle settings.
<br>
<br>The freestanding Flower Tab checks in Mushroo Way and Land's End will also be added.
<br>
<br>Boss fight locations will be available after you defeat the first iterations of those fights and also find the Stay Voucher. For example, you cannot do the postgame temple fight until after you have defeated the regular campaign temple fight, you can't use the Extra Shiny Stone until you've defeated the boss in the Monstro Town door the first time, etc."""
    _remake = False


# Delayed import to avoid circular dependency
from ..progression import prizelocations
from ..types.prizelocation import (
    PrizeLocation,
    BossFightLocation,
    StarPieceLocation,
)


def _location_class_to_attr_name(cls: type[PrizeLocation]) -> str:
    """Convert a PrizeLocation class to an attribute name for the enum."""
    # Use the class name, converting CamelCase to Snake_Case
    import re
    name = cls.__name__
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return name


class ItemCheckEnum(ClassCategorizationOption):
    """Enumeration for regular item check locations."""
    pass


class BossFightCheckEnum(ClassCategorizationOption):
    """Enumeration for boss fight check locations."""
    pass


class StarPieceCheckEnum(ClassCategorizationOption):
    """Enumeration for star piece check locations."""
    pass


# Populate the enums with location class types
for cls in vars(prizelocations).values():
    if isinstance(cls, type) and issubclass(cls, PrizeLocation) and hasattr(cls, "_id"):
        attr_name = _location_class_to_attr_name(cls)
        if issubclass(cls, StarPieceLocation) and cls is not StarPieceLocation:
            setattr(StarPieceCheckEnum, attr_name, cls)
        elif issubclass(cls, BossFightLocation) and cls is not BossFightLocation:
            setattr(BossFightCheckEnum, attr_name, cls)
        elif cls is not PrizeLocation and not issubclass(cls, (BossFightLocation, StarPieceLocation)):
            setattr(ItemCheckEnum, attr_name, cls)


class EnabledRegularChecks(CategorizationFlag[ItemCheckEnum]):
    _name = "General item pool checks"
    _description = """If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>This setting only applies if you have "Special Items can appear in the general item pool" or "Star Pieces can appear in the general item pool" enabled.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "chests"
    _default = {o: True for o in ItemCheckEnum.__members__.values()}


class EnabledBossChecks(CategorizationFlag[BossFightCheckEnum]):
    _name = "Boss fight checks"
    _description = """If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "bosses"
    _default = {o: True for o in BossFightCheckEnum.__members__.values()}


class EnabledStarPieceChecks(CategorizationFlag[StarPieceCheckEnum]):
    _name = "Star Piece checks"
    _description = """If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "stars"
    _default = {o: True for o in StarPieceCheckEnum.__members__.values()}


class ReplaceItems(BooleanFlag):
    _name = "Replace some chest items with coins"
    _description = "If enabled, the worst items (Wilt Shrooms, etc) will sometimes be replaced with coins in chests."
    _id = "replace"


# ✅
class PoisonMushroom(BooleanFlag):
    _name = "Change Fake Mushroom's Effect"
    _description = (
        "Randomize the status effect inflicted on a party member with the Fake Mushroom. It will only give "
        "one status effect per seed, which has a 1/8 chance of being Invincibility."
    )
    _id = "fake"


# ✅
class EXPChallengeOptions(CategorizationOption):
    """Enumeration for exp star quality scaling option"""

    VANILLA = "Vanilla"
    STARS = "Star Pieces"
    BOSSES = "Bosses"
    NONE = "None"


# ✅
class EXPChallenge(SelectOneFlag[EXPChallengeOptions]):
    _name = "EXP Star Behaviour"
    _description = """<b>Default</b>: EXP stars can give you 1 to 11 EXP per hit as normal.
<br>
<br><b>Star Pieces</b>: EXP per star increases with the number of Star Pieces collected.
<br>
<br><b>Bosses</b>: EXP per star increases with the number of bosses you have defeated.
<br>
<br><b>No EXP</b>: EXP stars give you 0 EXP."""
    choices = [o for o in EXPChallengeOptions]
    _default = EXPChallengeOptions.VANILLA
    _id = "xpstar"


# ✅
class GrateGuyPrizeThreshold(RangeFlag):
    _name = 'Required "Look The Other Way" wins'
    _description = "The number of times required to win Grate Guy's casino minigame to receive its ultimate prize."
    _default = 100
    min_value = 1
    max_value = 255
    _id = "gg"


# ✅
class KnifeGuyPrizeThreshold(RangeFlag):
    _name = "Required juggling wins"
    _description = "The number of wins minus losses required to win Knife Guy's ultimate juggling game prize."
    _default = 12
    min_value = 1
    max_value = 254
    _id = "kg"


# ✅
class SuitePrize1Threshold(RangeFlag):
    _name = "Required Suite prize #1 stays"
    _description = "The number of times required to stay in the Marrymore Suite to receive the first special gift"
    _default = 1
    min_value = 1
    max_value = 249
    _id = "s1"


# ✅
class SuitePrize2Threshold(RangeFlag):
    _name = "Required Suite prize #2 stays"
    _description = "The number of times required to stay in the Marrymore Suite to receive the second special gift"
    _default = 3
    min_value = 2
    max_value = 250
    _id = "s2"


# ✅
class SuitePrize3Threshold(RangeFlag):
    _name = "Required Suite prize #3 stays"
    _description = "The number of times required to stay in the Marrymore Suite to receive the third special gift"
    _default = 5
    min_value = 3
    max_value = 251
    _id = "s3"


# ✅
class SuitePrize4Threshold(RangeFlag):
    _name = "Required Suite prize #4 stays"
    _description = "The number of times required to stay in the Marrymore Suite to receive the fourth special gift"
    _default = 10
    min_value = 4
    max_value = 252
    _id = "s4"


# ✅
class SuitePrize5Threshold(RangeFlag):
    _name = "Required Suite prize #5 stays"
    _description = "The number of times required to stay in the Marrymore Suite to receive the fifth special gift"
    _default = 15
    min_value = 5
    max_value = 253
    _id = "s5"


# ✅
class SuitePrize6Threshold(RangeFlag):
    _name = "Required Suite prize #6 stays"
    _description = "The number of times required to stay in the Marrymore Suite to receive the sixth special gift"
    _default = 200
    min_value = 6
    max_value = 254
    _id = "s6"


# ✅
class SuperJump1Threshold(RangeFlag):
    _name = "Required Super Jumps for prize #1"
    _description = "The number of consecutive Super Jumps required for the first prize in Monstro Town"
    _default = 30
    min_value = 1
    max_value = 99
    _id = "sj1"


# ✅
class SuperJump2Threshold(RangeFlag):
    _name = "Required Super Jumps for prize #2"
    _description = "The number of consecutive Super Jumps required for the second prize in Monstro Town"
    _default = 100
    min_value = 2
    max_value = 100
    _id = "sj2"


# ******** Progression Gating


# ✅
class BanditsWayGating(CategorizationOption):
    """Enumeration for Bandit's Way gating flag option"""

    MALLOW = "Recruit Mallow"
    MUSHROOM_WAY = "Finish Mushroom Way"
    HAMMER_BRO = "Defeat Hammer Bros"
    OPEN = "Always open"


# ✅
class BanditsWayGate(SelectOneFlag[BanditsWayGating]):
    _name = """Bandit's Way access"""
    _description = """<b>Recruit Mallow</b>: Bandit's Way will become available on the world map when Mallow joins the party.
<br>
<br><b>Finish Mushroom Way</b>: Bandit's Way will become available on the world map when you defeat the boss of Mushroom Way.
<br>
<br><b>Defeat Hammer Bros</b>: Bandit's Way will become available on the world map when you have found and defeated the Hammer Bros boss battle.
<br>
<br><b>Always Open</b>: Bandit's Way will be available on the world map from the start of the game."""
    modes = ["open"]
    choices = [o for o in BanditsWayGating]
    _default = BanditsWayGating.MALLOW
    _id = "bw"


# ✅
class KeroSewersGating(CategorizationOption):
    """Enumeration for Bandit's Way gating flag option"""

    MALLOW = "Recruit Mallow"
    MACK = "Defeat Mack"
    KINGDOM = "Liberate Mushroom Kingdom"
    RFC = "Turn in the RareFrogCoin"
    OPEN = "Always open"


# ✅
class KeroSewersGate(SelectOneFlag[KeroSewersGating]):
    _name = """Kero Sewers access"""
    _description = """<b>Recruit Mallow</b>: The entrance to Kero Sewers will open when Mallow joins the party.
<br>
<br><b>Defeat Mack</b>: The entrance to Kero Sewers will open when you have found and defeated the Mack boss battle.
<br>
<br><b>Liberate Mushroom Kingdom</b>: The entrance to Kero Sewers will open when you have defeated the Mushroom Kingdom boss fight.
<br>
<br><b>Turn in the Rare Frog Coin</b>: The entrance to Kero Sewers will open when you turn in the Rare Frog Coin at the Mushroom Kingdom shop.
<br>
<br><b>Always Open</b>: The entrance to Kero Sewers is open from the start of the game.
<br>
<br>This setting does not affect your ability to enter via Land's End."""
    choices = [o for o in KeroSewersGating]
    _default = KeroSewersGating.OPEN
    _id = "ks"
    # SEWERS_CLOSED - set when game starts, cleared by condition. or just not set if always open


# ✅
class ForestMazeGating(CategorizationOption):
    """Enumeration for Forest Maze gating flag option"""

    PIE = "Exchange Cricket Pie"
    OPEN = "Always open"


# ✅
class ForestMazeGate(SelectOneFlag[ForestMazeGating]):
    _name = """Forest Maze access"""
    _description = """<b>Exchange Cricket Pie</b>: Forest Maze will become available on the world map when you turn in the Cricket Pie to Frogfucius.
<br>
<br><b>Always Open</b>: Forest Maze will be available on the world map from the start of the game."""
    choices = [o for o in ForestMazeGating]
    _default = ForestMazeGating.PIE
    _id = "fm"


# ✅
class PipeVaultGating(CategorizationOption):
    """Enumeration for Pipe Vault gating flag option"""

    GENO = "Recruit Geno"
    FOREST = "Finish Forest Maze"
    BOWYER = "Defeat Bowyer"
    OPEN = "Always open"


# ✅
class PipeVaultGate(SelectOneFlag[PipeVaultGating]):
    _name = """Pipe Vault access"""
    _description = """<b>Recruit Geno</b>: Pipe Vault will be unblocked when Geno joins the party.
<br>
<br><b>Finish Forest Maze</b>: Pipe Vault will be unblocked when you defeat the final boss of Forest Maze.
<br>
<br><b>Defeat Bowyer</b>: Pipe Vault will be unblocked when you have found and defeated the Bowyer boss battle.
<br>
<br><b>Always Open</b>: Pipe Vault will be unblocked from the start of the game."""
    choices = [o for o in PipeVaultGating]
    _default = PipeVaultGating.OPEN
    _id = "pv"


# ✅
class Moleville1Gating(CategorizationOption):
    """Enumeration for Pipe Vault gating flag option"""

    GENO = "Recruit Geno"
    FOREST = "Finish Forest Maze"
    BOWYER = "Defeat Bowyer"
    BOSHI = "Overthrow Boshi"
    OPEN = "Always open"


# ✅
class Moleville1Gate(SelectOneFlag[Moleville1Gating]):
    _name = """Moleville Mines entrance access"""
    _description = """<b>Recruit Geno</b>: The top door inside the Moleville Mines entrance will be accessible when Geno joins the party.
<br>
<br><b>Finish Forest Maze</b>: The top door inside the Moleville Mines entrance will be accessible when you defeat the final boss of Forest Maze.
<br>
<br><b>Defeat Bowyer</b>: The top door inside the Moleville Mines entrance will be accessible when you have found and defeated the Bowyer boss battle.
<br>
<br><b>Defeat Boshi</b>: The top door inside the Moleville Mines entrance will be accessible when you beat Boshi in a one-on-one race.
<br>
<br><b>Always Open</b>: The top door inside the Moleville Mines entrance will be accessible from the start of the game."""
    choices = [o for o in Moleville1Gating]
    _default = Moleville1Gating.OPEN
    _id = "me"


# ✅
class BoosterTowerGating(CategorizationOption):
    """Enumeration for Booster Tower gating flag option"""

    MARIO = "Recruit Mario"
    MALLOW = "Recruit Mallow"
    GENO = "Recruit Geno"
    BOWSER = "Recruit Bowser"
    TOADSTOOL = "Recruit Toadstool"
    MINES = "Finish Moleville Mines"
    PUNCHINELLO = "Defeat Punchinello"
    OPEN = "Always open"


# ✅
class BoosterTowerGate(SelectOneFlag[BoosterTowerGating]):
    _name = """Booster Tower access"""
    _description = """<b>Recruit character</b>: Booster Tower's door can be unlocked when you recruit the selected character.
<br>
<br><b>Finish Moleville</b>: Booster Tower's door will unlock when you defeat the final boss of Moleville.
<br>
<br><b>Defeat Punchinello</b>: Booster Tower's door will unlock when you have found and defeated the Punchinello boss battle.
<br>
<br><b>Always Open</b>: Booster Tower's door will be unlocked from the start of the game."""
    choices = [o for o in BoosterTowerGating]
    _default = BoosterTowerGating.BOWSER
    _id = "bt"


# ✅
class BoosterHillGating(CategorizationOption):
    """Enumeration for Booster Hill gating flag option"""

    TOWER = "Finish Booster Tower"
    KGGG = "Defeat Knife Guy & Grate Guy"
    OPEN = "Always open"


# ✅
class BoosterHillGate(SelectOneFlag[BoosterHillGating]):
    _name = """Booster Hill access"""
    _description = """<b>Finish Booster Tower</b>: The Booster Hill chase sequence will be available when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Defeat Knife Guy & Grate Guy</b>: The Booster Hill chase sequence will be available when you have found and defeated the Knife Guy & Grate Guy boss battle.
<br>
<br><b>Always Open</b>: The Booster Hill chase sequence will be available from the start of the game."""
    choices = [o for o in BoosterHillGating]
    _default = BoosterHillGating.OPEN
    _id = "bh"


# ✅
class MarrymoreGating(CategorizationOption):
    """Enumeration for Marrymore gating flag option"""

    HILL = "Finish Booster Hill"
    TOWER = "Finish Booster Tower"
    KGGG = "Defeat Knife Guy & Grate Guy"
    OPEN = "Always open"


# ✅
class MarrymoreGate(SelectOneFlag[MarrymoreGating]):
    _name = """Marrymore back door access"""
    _description = """<b>Finish Booster Hill</b>: The chapel back door will open when you complete Booster Hill one time.
<br>
<br><b>Finish Booster Tower</b>: The chapel back door will open when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Defeat Knife Guy & Grate Guy</b>: The chapel back door will open when you have found and defeated the Knife Guy & Grate Guy boss battle.
<br>
<br><b>Always Open</b>: The chapel back door will be open from the start of the game."""
    modes = ["open"]
    choices = [o for o in MarrymoreGating]
    _default = MarrymoreGating.HILL
    _id = "mm"


# ✅
class YaridovichGating(CategorizationOption):
    """Enumeration for Seaside boss gating flag option"""

    SHIP = "Finish Sunken Ship"
    JOHNNY = "Defeat Johnny"
    OPEN = "Always available"


# ✅
class YaridovichGate(SelectOneFlag[YaridovichGating]):
    _name = """Seaside boss fight access"""
    _description = """<b>Finish Sunken Ship</b>: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
<br>
<br><b>Defeat Johnny</b>: The Seaside boss fight will become available after you find and defeat the Johnny boss fight.
<br>
<br><b>Always Open</b>: The Seaside boss will be available from the start of the game."""
    choices = [o for o in YaridovichGating]
    _default = YaridovichGating.SHIP
    _id = "seaside"


# ✅
class SeaGating(CategorizationOption):
    """Enumeration for Sea & Sunken Ship gating flag option"""

    TOADSTOOL = "Recruit Toadstool"
    STAR_4 = "Collect 4 Star Pieces"
    BUNDT = "Defeat Bundt"
    MARRYMORE = "Finish Marrymore"
    OPEN = "Always open"


# ✅
class SeaGate(SelectOneFlag[SeaGating]):
    _name = """Sea & Sunken Ship access"""
    _description = """<b>Recruit Toadstool</b>: The Sea will become available on the world map when Toadstool joins the party.
<br>
<br><b>Collect 4 Star Pieces</b>: The Sea will become available on the world map when you collect 4 Star Pieces.
<br>
<br><b>Defeat Bundt</b>: The Sea will become available on the world map when you have found and defeated the Bundt boss battle.
<br>
<br><b>Always Open</b>: The Sea & Sunken Ship will be available on the world map from the start of the game."""
    choices = [o for o in SeaGating]
    _default = SeaGating.STAR_4
    _id = "sea"


# ✅
class LandsEndGating(CategorizationOption):
    """Enumeration for Land's End gating flag option"""

    STAR_5 = "Collect 5 Star Pieces"
    ELDER = "Rescue and talk to the Seaside Town elder"
    YARIDOVICH = "Defeat Yaridovich"
    SEASIDE = "Finish Seaside Town"
    OPEN = "Always open"


# ✅
class LandsEndGate(SelectOneFlag[LandsEndGating]):
    _name = """Land's End access"""
    _description = """<b>Collect 5 Star Pieces</b>: The cannon in Land's End will become usable when you collect 5 Star Pieces.
<br>
<br><b>Rescue and talk to the Seaside Town elder</b>: The cannon in Land's End will become usable on the world map when you rescue the elder in Seaside Town and speak with him. You will need to defeat the Sunken Ship boss and have the Shed Key to release the elder.
<br>
<br><b>Always Open</b>: The cannon in Land's End is usable from the start of the game."""
    choices = [o for o in LandsEndGating]
    _default = LandsEndGating.OPEN
    _id = "land"


# ✅
class BelomeTempleGating(CategorizationOption):
    """Enumeration for Belome Temple gating flag option"""

    KEY = "Use Temple Key"
    OPEN = "Always open"


# ✅
# no KI shuffle + closed monstro + use key = invalid, causes a softlock
class BelomeTempleGate(SelectOneFlag[BelomeTempleGating]):
    _name = """Belome Temple boss access"""
    _description = """<b>Use Temple Key</b>: The temple elevator will never lead to the boss fight until you dispel the Belome statue.
<br>
<br><b>Always Open</b>: The temple elevator works as normal."""
    choices = [o for o in BelomeTempleGating]
    _default = BelomeTempleGating.OPEN
    _id = "tmpl"


# ✅
class MonstroTownGating(CategorizationOption):
    """Enumeration for Monstro Town gating flag option"""

    LANDS_END = "Finish Land's End"
    BELOME_2 = "Defeat Belome 2"
    OPEN = "Always open"


# ✅
class MonstroTownGate(SelectOneFlag[MonstroTownGating]):
    _name = """Monstro Town access"""
    _description = """<b>Finish Land's End</b>: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
<br>
<br><b>Defeat Belome 2</b>: Monstro Town will become available on the World Map when you have found and defeated the Belome 2 boss battle. The pipe in Land's End will be blocked until this happens.
<br>
<br><b>Always Open</b>: Monstro Town will be available on the World Map from the start of the game."""
    choices = [o for o in MonstroTownGating]
    _default = MonstroTownGating.LANDS_END
    _id = "mt"


# ✅
class SkipMustyFearsSequence(BooleanFlag):
    _name = "Skip 3 Musty Fears sequence"
    _description = """This flag affects the Musty Fears checks (normally Mario's Pad bed, Rose Town sign, and Yo'ster Isle goalpost; or whichever three locations are added to the seed when "Move invisible flag checks" is set).
<br>
<br>If disabled, the affected checks will become available after you visit the Musty Fears Inn in Monstro Town.
<br>
<br>If enabled, the affected checks will be available from the start of the seed."""
    _id = "skip_musty"


# ✅
class NimbusGating(CategorizationOption):
    """Enumeration for Nimbus Land gating flag option"""

    VALLEY = "Finish Bean Valley"
    MEGASMILAX = "Defeat Megasmilax"
    PAINT = "Find Gold Paint"
    OPEN = "Always open"


# ✅
class NimbusGate(SelectOneFlag[NimbusGating]):
    _name = """Nimbus Land access"""
    _description = """<b>Finish Bean Valley</b>: The trampoline to Nimbus Land will be enabled once you defeat the boss of Bean Valley.
<br>
<br><b>Defeat Megasmilax</b>: The trampoline to Nimbus Land will be enabled when you have found and defeated the Megasmilax boss battle.
<br>
<br><b>Find Gold Paint</b>: The trampoline to Nimbus Land is enabled by default, but you will need to find an item called "Gold Paint" before Garro will take you into the castle.
<br>
<br><b>Always Open</b>: Nimbus Land and its castle are open from the start of the game."""
    choices = [o for o in NimbusGating]
    _default = NimbusGating.OPEN
    _id = "nl"


# ✅
class BarrelVolcanoGating(CategorizationOption):
    """Enumeration for Barrel Volcano gating flag option"""

    NIMBUS = "Finish Nimbus Land"
    VALENTINA = "Defeat Valentina"
    OPEN = "Always open"


# ✅
class BarrelVolcanoGate(SelectOneFlag[BarrelVolcanoGating]):
    _name = """Barrel Volcano access"""
    _description = """<b>Finish Nimbus Land</b>: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
<br>
<br><b>Defeat Valentina</b>: Barrel Volcano will become available on the World Map when you have found and defeated the Valentina boss battle.
<br>
<br><b>Always Open</b>: Barrel Volcano will be available on the World Map from the start of the game."""
    choices = [o for o in BarrelVolcanoGating]
    _default = BarrelVolcanoGating.NIMBUS
    _id = "bv"


# ✅
class BowsersKeepGating(CategorizationOption):
    """Enumeration for Bowser's Keep gating flag option"""

    STAR_6 = "Collect 6 Star Pieces"
    VOLCANO = "Finish Barrel Volcano"
    AXEM = "Defeat Axem Rangers"
    OPEN = "Always open"


# ✅
class BowsersKeepGate(SelectOneFlag[BowsersKeepGating]):
    _name = """Bowser's Keep access"""
    _description = """<b>Collect 6 Star Pieces</b>: Bowser's Keep will become available on the world map when you collect 6 Star Pieces.
<br>
<br><b>Finish Barrel Volcano</b>: Bowser's Keep will become available on the World Map once you defeat the final boss of Barrel Volcano.
<br>
<br><b>Defeat Axem Rangers</b>: Bowser's Keep will become available on the World Map when you have found and defeated the Axem Rangers boss battle.
<br>
<br><b>Always Open</b>: Bowser's Keep will be available on the world map from the start of the game."""
    choices = [o for o in BowsersKeepGating]
    _default = BowsersKeepGating.VOLCANO
    _id = "bk"


# ✅
class FactoryGating(CategorizationOption):
    """Enumeration for Factory gating flag option"""

    OPEN = "Open when Bowser's Keep is opened"
    KEEP = "Finish Bowser's Keep"
    STAR_6 = "Collect 6 Star Pieces"
    EXOR = "Defeat Exor"


# ✅
class FactoryGate(SelectOneFlag[FactoryGating]):
    _name = """Factory access"""
    _description = """<b>Open when Bowser's Keep is opened</b>: When Bowser's Keep becomes available on the world map, Factory will also be immediately available on the world map.
<br>
<br><b>Finish Bowser's Keep</b>: Factory will become available on the world map when you complete Bowser's Keep for the first time.
<br>
<br><b>Defeat Exor</b>: Factory will become available on the World Map when you have found and defeated the Exor boss battle and Bowser's Keep has been opened.
<br>
<br><b>Collect 6 Star Pieces</b>: Factory will become available on the world map when you collect 6 Star Pieces and Bowser's Keep has been opened."""
    choices = [o for o in FactoryGating]
    _default = FactoryGating.KEEP
    _id = "wf"


# ✅
class BowserDoorRequirements(RangeFlag):
    _name = "Required Bowser's Keep obstacle doors"
    _description = "The number of doors required to progress through Bowser's Keep."
    _default = 4
    min_value = 1
    max_value = 6
    _id = "doors"


# ✅
class StarPiecesRequired(RangeFlag):
    _name = "Star Pieces required to access the final Factory boss"
    _description = "The total number of Star Pieces (0-7) that are required to access the final boss (enables the green button in Inner Factory). Cannot be higher than Total Star Pieces."
    _default = 6
    min_value = 0
    max_value = 7
    _id = "endgame"


# ✅
class CasinoWarp(BooleanFlag):
    _name = "Casino Warp"
    _description = """If enabled, a trampoline warping directly to the final boss fight will become available in Grate Guy's Casino."""
    _id = "cwarp"


# ✅
class BucketWarp(BooleanFlag):
    _name = "Bucket Warp"
    _description = "If enabled, trading a Carbo Cookie to the bucket girl in Moleville will reveal a warp to the final boss fight."
    _id = "bwarp"


# ✅
class FastTravel(BooleanFlag):
    _name = "Fast travel"
    _description = """If enabled, the following features will be enabled:
<ol>
<li>The Booster Tower balcony (after defeating the boss) will always return you to the ground level.</li>
<li>Inner Factory has a trampoline that exits to the world map.</li>
<li>When you first reach the Inner Factory from the Outer Factory, the Inner Factory will get an entrance dot on the world map.</li>
</ol>"""
    _id = "fasttravel"


# ✅
class WinConditions(CategorizationOption):
    """Enumeration for win condition options"""

    FACTORY = "Beat the final Factory boss"
    SMITHY = "Beat Smithy"
    STARS = "Collect required Star Pieces"
    SEALED = "Beat Monstro Town sealed door"


# ✅
class WinCondition(SelectOneFlag[WinConditions]):
    _name = "Condition required to beat the game"
    _description = """<b>Beat the Factory</b>: When you collect the number of Star Pieces specified in your 'Star Pieces required to access the final Factory boss' setting, the button in the Inner Factory (as well as any enabled warps) will be enabled to allow you to access the final boss and beat the game.
<br>
<br><b>Beat Smithy</b>: The game is over as soon as you find Smithy and defeat him. (If you don't have him shuffled into the boss pool, this is the same thing as "Beat the Factory".)
<br>
<br><b>Collect required Star Pieces</b>: As soon as you collect the number of Star Pieces specified in your 'Star Pieces required to access the final Factory boss' setting, the game is finishe regardless of where you found your final Star Piece.
<br>
<br><b>Beat Monstro Town sealed door</b>: The game is over when you defeat the boss behind the sealed door in Monstro Town, regardless of your Star Piece count."""
    choices = [o for o in WinConditions]
    _default = WinConditions.FACTORY
    _id = "objective"


# ******** Puzzles


class BallSolitaireShuffle(BooleanFlag):
    _name = "Randomize Ball Solitaire"
    _description = "The layout for the Ball Solitaire minigame will be randomized."
    _id = "ball"


class MagicButtonShuffle(BooleanFlag):
    _name = "Randomize Magic Buttons"
    _description = "The layout for the Magic Buttons minigame will be randomized."
    _id = "button"


class QuizShuffle(BooleanFlag):
    _name = "Randomize Dr. Topper Quiz"
    _description = "The question pool for the Dr. Topper quiz will include new questions submitted by players."
    _id = "quiz"


class RandomTadpolePondSong(BooleanFlag):
    _name = "Randomize Tadpole Pond songs"
    _description = """If enabled, the songs required for the three Tadpole Pond songs will be selected from a pool (submitted by players). Hints will be available in their normal locations within Tadpole Pond, Moleville Mines, and Monstro Town."""
    _id = "melody"


class RandomSunkenShipPassword(BooleanFlag):
    _name = "Randomize Sunken Ship password"
    _description = """If enabled, the password for the Sunken Ship will be selected from a pool (submitted by players). Hints are available in the 6 ship puzzles, and occasionally on posted notes within the Sunken Ship.
<br/>
<br/><b>Be warned that some of these are very difficult, or may be references to things you aren't familiar with, but they are all solvable.</b> The nearby shop shaman will tell you how many of your letters were correct when you submit an incorrect password."""
    _id = "pwd"


class BowserDoorShuffle(BooleanFlag):
    _name = "Randomize Bowser's Keep room sequences"
    _description = """If enabled, the 18 rooms making up the six Bowser's Keep obstacle course doors will be shuffled into six random sequences of three rooms each."""
    _id = "doors"


class SkipMinecart(BooleanFlag):
    _name = "Skip Minecart minigame"
    _description = """If enabled, boarding the minecart for the first time will teleport you back to Moleville. Subsequent visits to the minecart room will play the minigame as normal."""
    _id = "skipcart"


class BetterTips(BooleanFlag):
    _name = "Better Event RNG"
    _description = """If enabled, the following changes will take effect:
<br/>
<br/>Some repeatable item grants will give a better, or wider, variety of items. Example of this include Knife Guy's juggling game junk prizes, or tips from working in the Marrymore hotel. This setting has no impact on singular, clearable item checks.
<br/>
<br/>Your odds on Mushroom Boy's prizes and the Mushroom Derby cookie bet races will be improved.
<br/>
<br/>The cloud miniboss in Land's End will have an increased spawn rate. 
<br/>
<br/>Forest Maze mushrooms may be ANY kind of mushroom.
    """
    _id = "rng"


# ******** Shops


# if this is disabled, no options in this category can be changed

# TODO All frog disciple items should NOT be randomized if ShuffleShops is off.
# ✅
class ShuffleShops(BooleanFlag):
    _name = "Randomize the contents of shops"
    _description = """If enabled, the contents of all regular shops and Frog Coin shops (including the Moleville treasure shop, Marrymore Suite room service menu, and Moleville swap shop) will be randomized."""
    _id = "random"


# ✅
class ShopQualities(CategorizationOption):
    """Enumeration for shop shuffle quality option"""

    ORIGINAL = "Original shop pool"
    COMPLETELY_RANDOM = "Completely random items"
    MOSTLY_RANDOM = "Random items, biased toward low-impact items"
    EMPTY = "Completely empty"


# ✅
class ShopQuality(SelectOneFlag[ShopQualities]):
    _name = """Shop contents quality"""
    _description = """Restricts the incidence of certain items in shops. 
<br>
<br>"Completely random" means that some items which originally did not appear in shops may now appear in shops, but only a small pool of items are guaranteed to appear. Some items will never appear in non-depletable shops. 
<br>
<br>If "Completely empty" is selected, all shops will just sell the Goodie Bag."""
    choices = [o for o in ShopQualities]
    _default = ShopQualities.ORIGINAL
    _id = "quality"
    _requires_all = [(ShuffleShops(), True)]


# ✅
class BiasShopShuffle(BooleanFlag):
    _name = "Bias better items to gated shops"
    _description = (
        """If enabled, harder-to-reach shops will generally sell better items."""
    )
    _id = "bias"
    _requires_all = [
        (ShuffleShops(), True),
        (ShopQuality(), [o for o in ShopQualities if o != ShopQualities.ORIGINAL]),
    ]


# ✅
class NoPickMeUps(BooleanFlag):
    _name = "Exclude Pick Me Ups"
    _description = """If enabled, Pick Me Ups will not be sold in any shops."""
    _id = "nolife"


# ✅
class ShowEquips(BooleanFlag):
    _name = "Always show all permitted characters on equips"
    _description = "Always show who can equip what in stores."
    _id = "showperms"
    _default = True


# ✅
class FreeShops(BooleanFlag):
    _name = "'Free' Shops"
    _description = """If enabled, all shop items will cost 1 coin. You will start with 9999 coins and 999 frog coins."""
    _id = "free"


# ******** Enemies & Bosses


class BossShuffle(BooleanFlag):
    _name = "Randomize boss fight locations"
    _description = "If enabled, the positions of bosses (plus Pandorite, Hidon, Box Boy, Chester, and Mokura) are shuffled."
    _id = "random"
    # if false, disable stat scaling and mimics anywhere


class BossScaleOptions(CategorizationOption):
    """Enumeration for shuffled boss stat scaling"""

    VANILLA = "Do not scale"
    MATCH = "Match to area"
    RANDOM = "Completely random"


class BossShuffleScaleStats(SelectOneFlag[BossScaleOptions]):
    _name = "Scale boss stats"
    _description = """<b>Do not scale</b>: Boss fights retain their relative original stats, regardless of where they are placed. For example, Culex would still have around 4000 HP, even if he's in Mushroom Way.
<br>
<br><b>Match to area</b>: A boss fight that has been shuffled into a different area will have its stats scaled to match the area's original boss. For example, Culex would have about 100 HP if he's in Mushroom Way.
<br>
<br><b>Completely random</b>: A boss fight will inherit the relative stats of a random other location, regardless of position. For example, Culex could be placed in Mushroom Way, but have 1200 HP because he's inherited Belome 2's original stats."""
    choices = [o for o in BossScaleOptions]
    _default = BossScaleOptions.VANILLA
    _id = "scale"


class BossReplaceMinigameSprites(BooleanFlag):
    _name = "Replace important NPCs to match shuffled bosses"
    _description = """If enabled: All sprites related to an area boss will be changed to match the shuffled positions of bosses.
<br>
<br>If disabled: Some sprites will be left unchanged from the original game to accommodate visual cues (such as the Booster Hill snifits, or Dodo in his statue room) or progression knowledge on required sub-fights (such as the Bandana Reds in Sunken Ship)."""
    _id = "allsprites"
    _default = True


class DifferentiateRepeatedBosses(BooleanFlag):
    _name = "Differentiate similar bosses"
    _description = """If enabled, Croco, Jinx, Belome, and the four mimics (as well as Punchinello, Johnny, Bundt, Culex, and Booster if remake content is enabled) will look slightly different in the overworld depending on which version of the fight it is. 
<br>
<br>Croco 2 will have a darker hat.
<br>
<br>Jinx 2/3's hair will be black/white respectively.
<br>
<br>Belome 2 will be more subdued, and coloured like the golden Belome statue.
<br>
<br>Pandorite will be tinted orange, Hidon will be tinted green, and Chester will be tinted purple."""
    _id = "diff"
    # TODO: belome 3, punchinello 2, jinx 4, johnny 2, bundt 2, culex 3D, booster 2


class IncludeHenchmen(BooleanFlag):
    _name = "Change henchman battles to match boss fights"
    _description = """If enabled, the battles with Shysters in Mushroom Kingdom, Snifits in Booster Tower, Crooks in Moleville Mines, and Bandana Reds in the Sunken Ship may be replaced with other monsters depending on the corresponding boss location. For example, if Culex is the first tower boss, you might fight a Crystal on your way up the tower instead of a Snifit."""
    _id = "henchmen"
    _default = True


class ShuffledBossEnum(ClassCategorizationOption):
    """Enumeration for all boss fights that can be shuffled"""

    pass


# Populate ShuffledBossEnum with boss fight class types
def _boss_class_to_attr_name(boss_class: type[BossFightPrize]) -> str:
    """Convert boss class name to an attribute name.

    Examples:
        Croco1BossFight -> Croco_1
        KnifeGuyGrateGuyBossFight -> Knife_Guy_Grate_Guy
        Culex3DBossFight -> Culex_3D
    """
    import re

    name = boss_class.__name__
    # Remove BossFight/Fight suffix
    name = re.sub(r"(BossFight|Fight|Dight)$", "", name)
    # Add spaces before capital letters and numbers
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", name)
    name = re.sub(r"(\d+)", r" \1", name)
    # Clean up multiple spaces and convert to underscores
    name = re.sub(r"\s+", " ", name).strip()
    return name.replace(" ", "_").replace("-", "_")


for boss_class in ALL_BOSS_FIGHTS:
    attr_name = _boss_class_to_attr_name(boss_class)
    setattr(ShuffledBossEnum, attr_name, boss_class)


class ShuffledBosses(CategorizationFlag[ShuffledBossEnum]):
    _name = "Shuffled boss fights"
    _description = """Each boss fight location below stats the enemy that originally inhabits it.
<br>
<br>If a location is highlighted (white text over blue), there will instead be a random different boss inhabiting that location.
<br>
<br>If a boss is not highlighted, the location's original boss fight will stay there.
<br>
<br>Selecting a remake-specific boss will do nothing if the remake flag is not enabled."""
    _id = "pool"
    _default = {o: True for o in ShuffledBossEnum.__members__.values()}


# ✅
class EnemyStatsShuffleOptions(CategorizationOption):
    """Enumeration for enemy stat randomization option"""

    DISABLED = "Original stats"
    NUMBERS_ONLY = "Stat values only"
    FULL_RANDOM = "Everything"


# ✅
class EnemyStats(SelectOneFlag[EnemyStatsShuffleOptions]):
    _name = "Randomize enemy stats"
    _description = """Choose what should be randomized about enemy stats (includes normal mobs and bosses).
<br>
<br><bold>Stat values only</bold>: Attack, defense, speed, and HP values are randomized. Elemental weaknesses/resistances and status immunities remain unchanged.
<br>
<br><bold>Everything</bold>: Attack, defense, speed, and HP values are randomized. Elemental weaknesses/resistances and status immunities are also randomized.
<br>
<br><b>Original stats</b>: Enemy stats remain unchanged."""
    _id = "scale"
    choices = [o for o in EnemyStatsShuffleOptions]
    _default = EnemyStatsShuffleOptions.DISABLED


# ✅
class EnemyDrops(BooleanFlag):
    _name = "Randomize enemy drops"
    _description = "If enabled, the EXP and in-battle items received from battles will be randomized."
    _id = "drops"


# ✅
class EnemyFormations(BooleanFlag):
    _name = "Randomize formations"
    _description = """If enabled, enemy encounters may contain random unexpected additional enemies and be laid out erratically. Boss formations are not affected.
<br>
<br>Note: If you've chosen to enable shuffled henchman battles, those formations are always randomized independent of this setting."""
    _id = "formations"


# ✅
class EnemyAttacks(BooleanFlag):
    _name = "Randomize attack stats and effects"
    _description = "If enabled, enemy spells and attacks will have their power randomized. Attacks which cast statuses will have the status effects randomized, and attacks which normally don't inflict statuses may inflict unexpected statuses."
    _id = "attacks"


# ✅
class EnemySpells(BooleanFlag):
    _name = "Randomize enemy spell assignments"
    _description = "If enabled, enemies can cast random spells (excluding remake spells). I.E. Mack could cast Blast instead of Flame."
    _id = "spells"


# ✅
class ExperienceNoRegular(BooleanFlag):
    _name = "Remove EXP from regular enemy encounters"
    _description = "If enabled, regular enemy encounters will not give any EXP when defeated. Boss fights are not affected by this flag."
    _id = "noregexp"


# ✅
class ExperienceNoBosses(BooleanFlag):
    _name = "Remove EXP from boss encounters"
    _description = "If enabled, boss encounters will not give any EXP when defeated. Regular enemy encounters are not affected by this flag."
    _id = "nobossexp"


# ✅
class SkipBossFights(BooleanFlag):
    _name = "Allow alternate boss fight win conditions"
    _description = """If set, the following actions will allow you to skip a boss fight and still proceed as normal:
<ul>
<li> Mack Skip</li>
<li> Booster Tower curtain game</li>
<li> Nimbus Castle statue game</li>
</ul>
<br/>If unset, you must still fight the associated boss to receive Star Pieces and other rewards."""
    _id = "skips"
    _default = True


# ✅
class NoGenoWhirlExor(BooleanFlag):
    _name = "No Geno Whirl on Exor"
    _description = (
        "If enabled, stunning Exor's eyes will not make him vulnerable to Geno Whirl."
    )
    _id = "nowhirl"


# ✅
class FixMagikoopa(BooleanFlag):
    _name = "Fix Magikoopa"
    _description = (
        "If enabled, King Bomb's Big Bang will not disable Magikoopa's attacks."
    )
    _id = "nobigbang"


# ✅
class NoOHKO(BooleanFlag):
    _name = "No instant KOs on boss allies"
    _description = (
        "You will not be able to use Geno Whirl, Pure Water, or Lamb's Lure/Sheep Attack to OHKO any allies to a boss (Mallow Clone, "
        "Bandana Blue, Fautso, etc)."
    )
    _id = "noko"


# ******** Cosmetics and Accessibility
# aka stuff that doesn't affect the seed


# ✅
class PaletteSwaps(BooleanFlag):
    _name = "Palette Swaps"
    _description = "Your party members get a change of wardrobe!"
    _id = "palette"


# ✅
class ChangeNames(BooleanFlag):  # not available unless PaletteSwaps enabled
    _name = "Change character names"
    _description = """Some palette swaps are references to other media. If this flag is enabled, the character's name will be changed to match the palette."""
    _id = "names"


# ✅
class RemakeNames(BooleanFlag):
    _name = "Use Remake Names"
    _description = "Spells, enemies, items, and attacks will use their names from the 2023 Switch remake (where space limits allow)."
    _id = "remake"


# ✅
class CanonNames(BooleanFlag):
    _name = "Use Canon Names"
    _description = "Magikoopa is renamed 'Kamek' and Birdo is renamed 'Birdetta'."
    _id = "canon"


# ✅
class Peach(BooleanFlag):
    _name = "Rename Peach"
    _description = (
        "Toadstool is renamed 'Peach' (overridden by palette name swaps, if enabled)."
    )
    _id = "peach"


# ✅
class JapaneseABXY(BooleanFlag):
    _name = "Japanese ABXY buttons"
    _description = "If this flag is enabled, ABXY buttons will have the Super Famicom colours from the Japanese version of the game instead of the SNES purple."
    _id = "abxy"


# ✅
class BossShuffleMusic(BooleanFlag):
    _name = "Randomize boss music"
    _description = "Battle music will be randomized for each boss fight."
    _id = "music"


# ✅
from smrpgpatchbuilder.datatypes.battles.music import (
    NormalBattleMusic,
    MidbossMusic,
    BossMusic,
    Smithy1Music,
    CorndillyMusic,
    BoosterHillMusic,
    VolcanoMusic,
    CulexMusic,
)


# ✅
class ShuffledMusicEnum(ClassCategorizationOption):
    """Enumeration for all battle music tracks that can be shuffled."""

    NORMAL_BATTLE = NormalBattleMusic
    MIDBOSS = MidbossMusic
    BOSS = BossMusic
    SMITHY_1 = Smithy1Music
    CORNDILLY = CorndillyMusic
    BOOSTER_HILL = BoosterHillMusic
    VOLCANO = VolcanoMusic
    CULEX = CulexMusic


# ✅
class ShuffledMusic(CategorizationFlag[ShuffledMusicEnum]):
    _name = "Allowable shuffled music"
    _description = """If a song is highlighted (white text over blue), it can appear in any boss fight.
<br>
<br>If a song is not highlighted, it will never appear in a boss fight.
<br>
<br>This setting does nothing if "Randomize boss music" is turned off."""
    _id = "avail"
    _default = {o: True for o in ShuffledMusicEnum.__members__.values()}


# ✅
class RemoveFlashes(BooleanFlag):
    _name = "Remove flashes"
    _description = """Removes some flashing animations (from spells, attacks, etc). 
<br>
<br>Disclaimer: While this feature is intended to promote accessibility, SMRPG Randomizer's developers are not accessibility experts and we may have missed some things. Players and viewers with photosensitivity should continue to engage with this randomizer at their own risk. If you would like to suggest an animation that should have flashes removed by this feature, please see the "Contributing" section and fill out the form."""
    _id = "noflash"


# ✅
class HoldB(BooleanFlag):
    _name = "Hold B to auto-advance text"
    _description = "Holding the B button will advance text boxes."
    _id = "holdb"


#############


class FlagCategory:
    """Base class for a collection of settings."""

    _id: str = ""
    _name: str = ""
    _subcategories: "list[type[FlagCategory]]" = []
    _flags: list[type[Flag]] = []
    _size: int = 3

    @property
    def id(self) -> str:
        """An identifier for this collection to use internally."""
        return self._id

    @property
    def name(self) -> str:
        """An identifier for this collection to appear in the frontend."""
        return self._name

    @property
    def subcategories(self) -> "list[type[FlagCategory]]":
        """Subcategories for this collection."""
        return self._subcategories

    @property
    def flags(self) -> list[type[Flag]]:
        """Individual settings that belong in this collection."""
        return self._flags

    @property
    def size(self) -> int:
        """Something to do with the frontend that I don't remember"""
        return self._size


class CharacterRecruitmentSubcategory(FlagCategory):
    """Collection of settings related to character recruitment."""

    _flags: list[type[Flag]] = [
        ShuffleCharacters,
        MaxCharacters,
        StartingCharacters,
        PlayAsStarter,
    ]
    _size: int = 4
    _id: str = "P"


class CharacterEquipmentSubcategory(FlagCategory):
    """Collection of settings related to equipment properties."""

    _flags: list[type[Flag]] = [
        EquipmentCharacters,
        EquipmentProperties,
        IgnoreNamesakeProperties,
        StarPieceHints,
    ]
    _size: int = 4
    _id: str = "Q"


class CharacterStatsSpellsSubcategory(FlagCategory):
    """Collection of settings related to learnable spells."""

    _flags: list[type[Flag]] = [
        EXPMultiplier,
        CharacterStats,
        CharacterLearnedSpells,
        CharacterSpellStats,
        InfuseSpellElements,
        CharacterSpellElements,
        UncapSuperJumps,
        AvailableSpells,
    ]


class PartyCategory(FlagCategory):
    """Pan-collection of settings related to party members and equips."""

    _name: str = "Party & Equipment"
    _subcategories: list[type[FlagCategory]] = [
        CharacterRecruitmentSubcategory,
        CharacterEquipmentSubcategory,
        CharacterStatsSpellsSubcategory,
    ]
    _id: str = "PartyCategory"


class StarPiecesCategory(FlagCategory):
    """Collection of settings related to star piece distribution."""

    _flags: list[type[Flag]] = [
        ShuffleStarPieces,
        TotalStarPieces,
        EnabledBossChecks,
        ProgressionLogicDifficulty,
        DisperseStarPieces,
    ]
    _size: int = 3
    _id: str = "X"


class ItemShuffleSubcategory(FlagCategory):
    """Collection of settings related to item distribution."""

    _flags: list[type[Flag]] = [
        ShuffleItems,
        ItemQuality,
        BiasItemShuffle,
        NoStarEgg,
        RestrictSpecialEquips,
        EXPStarsAnywhere,
        MimicsAnywhere,
        SlotsAnywhere,
        ShuffleBeetlemania,
        ShuffleMagikoopaChest,
        ShuffleWeddingGear,
        AnnoyingChests,
        FireworksSetting,
    ]
    _id: str = "T"


class ItemLocationSubcategory(FlagCategory):
    """Collection of settings related to item availability."""

    _flags: list[type[Flag]] = [
        KeyItemsAnywhere,
        StarPieceAvailability,
        InvisibleFlagsSetting,
        Remake,
        EnabledRegularChecks,
    ]
    _id: str = "L"


class BehaviourSubcategory(FlagCategory):
    """Collection of settings related to item and minigame behaviour."""

    _flags: list[type[Flag]] = [
        ReplaceItems,
        PoisonMushroom,
        EXPChallenge,
        GrateGuyPrizeThreshold,
        KnifeGuyPrizeThreshold,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
        SuperJump1Threshold,
        SuperJump2Threshold,
    ]
    _id: str = "I"


class ItemsCategory(FlagCategory):
    """Pan-collection of settings related to items."""

    _name: str = "Items & Star Pieces"
    _subcategories: list[type[FlagCategory]] = [
        StarPiecesCategory,
        ItemShuffleSubcategory,
        ItemLocationSubcategory,
        BehaviourSubcategory,
    ]
    _id: str = "ItemsCategory"


class AreaAccessSubcategory(FlagCategory):
    """Collection of settings related to area gating logic."""

    _flags: list[type[Flag]] = [
        BanditsWayGate,
        KeroSewersGate,
        ForestMazeGate,
        PipeVaultGate,
        Moleville1Gate,
        BoosterTowerGate,
        BoosterHillGate,
        MarrymoreGate,
        SeaGate,
        LandsEndGate,
        BelomeTempleGate,
        MonstroTownGate,
        NimbusGate,
        BarrelVolcanoGate,
        BowsersKeepGate,
        FactoryGate,
    ]
    _size: int = 3
    _id: str = "A"


class OtherAccessSubcategory(FlagCategory):
    """Collection of settings related to event gating logic."""

    _flags: list[type[Flag]] = [
        YaridovichGate,
        SkipMustyFearsSequence,
        BowserDoorRequirements,
        StarPiecesRequired,
        CasinoWarp,
        BucketWarp,
        FastTravel,
        WinCondition,
    ]
    _size: int = 3
    _id: str = "O"


class PuzzleCategory(FlagCategory):
    """Collection of settings related to puzzles."""

    _name: str = "Puzzles & Minigames"
    _flags: list[type[Flag]] = [
        BallSolitaireShuffle,
        MagicButtonShuffle,
        QuizShuffle,
        RandomTadpolePondSong,
        RandomSunkenShipPassword,
        BowserDoorShuffle,
        SkipMinecart,
        BetterTips,
    ]
    _size: int = 3
    _id: str = "G"


class ShopsCategory(FlagCategory):
    """Collection of settings related to shops."""

    _flags: list[type[Flag]] = [
        ShuffleShops,
        ShopQuality,
        BiasShopShuffle,
        NoPickMeUps,
        ShowEquips,
        FreeShops,
    ]
    _size: int = 3
    _id: str = "S"


class AccessCategory(FlagCategory):
    """Pan-collection of settings related to logical access and puzzles."""

    _name: str = "Progression & Shops"
    _subcategories: list[type[FlagCategory]] = [
        AreaAccessSubcategory,
        OtherAccessSubcategory,
        PuzzleCategory,
        ShopsCategory,
    ]
    _id: str = "AccessCategory"


class BossPositionSubcategory(FlagCategory):
    """Collection of settings related to boss placement."""

    _flags: list[type[Flag]] = [
        BossShuffle,
        BossShuffleScaleStats,
        BossReplaceMinigameSprites,
        DifferentiateRepeatedBosses,
        IncludeHenchmen,
        ShuffledBosses,
    ]
    _size: int = 4
    _id: str = "B"


class BossStatSubcategory(FlagCategory):
    """Collection of settings related to enemy stats."""

    _flags: list[type[Flag]] = [
        EnemyStats,
        EnemyDrops,
        EnemyFormations,
        EnemyAttacks,
        EnemySpells,
        ExperienceNoRegular,
        ExperienceNoBosses,
    ]
    _size: int = 4
    _id: str = "E"


class BossCheeseSubcategory(FlagCategory):
    """Collection of settings related to boss exploits."""

    _flags: list[type[Flag]] = [
        SkipBossFights,
        NoGenoWhirlExor,
        FixMagikoopa,
        NoOHKO,
    ]
    _size: int = 4
    _id: str = "F"


class BossCategory(FlagCategory):
    """Pan-collection of settings related to bosses."""

    _name: str = "Enemies & Boss Fights"
    _subcategories: list[type[FlagCategory]] = [
        BossPositionSubcategory,
        BossStatSubcategory,
        BossCheeseSubcategory,
    ]
    _id: str = "BossCategory"


class AccessibilitySubcategory(FlagCategory):
    """Collection of settings related to accessibility."""

    _flags: list[type[Flag]] = [RemoveFlashes, HoldB]
    _size: int = 3
    _id: str = "R"


class MusicSubcategory(FlagCategory):
    """Collection of settings related to music cosmetics."""

    _flags: list[type[Flag]] = [BossShuffleMusic, ShuffledMusic]
    _size: int = 3
    _id: str = "R"


class PaletteSubcategory(FlagCategory):
    """Collection of settings related to visual cosmetics."""

    _flags: list[type[Flag]] = [
        PaletteSwaps,
        JapaneseABXY,
    ]
    _size: int = 3
    _id: str = "R"


class NamesCategory(FlagCategory):

    _flags: list[type[Flag]] = [ChangeNames, RemakeNames, CanonNames, Peach]
    _size: int = 3
    _id: str = "R"


class CosmeticCategory(FlagCategory):
    """Pan-collection of settings related to things that don't affect logic."""

    _name: str = "Cosmetics"
    _subcategories: list[type[FlagCategory]] = [
        AccessibilitySubcategory,
        MusicSubcategory,
        PaletteSubcategory,
        NamesCategory,
    ]


FlagCategoryT = TypeVar(
    "FlagCategoryT",
    CharacterRecruitmentSubcategory,
    CharacterEquipmentSubcategory,
    CharacterStatsSpellsSubcategory,
    PartyCategory,
    StarPiecesCategory,
    ItemShuffleSubcategory,
    ItemLocationSubcategory,
    BehaviourSubcategory,
    ItemsCategory,
    AreaAccessSubcategory,
    OtherAccessSubcategory,
    PuzzleCategory,
    ShopsCategory,
    AccessCategory,
    BossPositionSubcategory,
    BossStatSubcategory,
    BossCheeseSubcategory,
    BossCategory,
    AccessibilitySubcategory,
    MusicSubcategory,
    PaletteSubcategory,
    NamesCategory,
    CosmeticCategory,
    FlagCategory,
)

CATEGORIES = (
    PartyCategory,
    ItemsCategory,
    AccessCategory,
    BossCategory,
    CosmeticCategory,
)
