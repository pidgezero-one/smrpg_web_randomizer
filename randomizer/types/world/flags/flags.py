# pylint: disable=C0301

"""Randomizer setting definitions."""

from typing import List

from randomizer.types.bosses import BossLocations

from .categorizations import (
    BANDITS_WAY_GATING_LIST,
    BOSS_MUSIC_LIST,
    BOSS_SCALE_LIST,
    BOSS_STAR_PIECE_LOCATIONS,
    EQUIPMENT_CHARACTERS_LIST,
    EQUIPMENT_PROPERTIES_LIST,
    EXP_CHALLENGE_OPTIONS_LIST,
    EXP_MULTIPLIER_OPTIONS,
    FACTORY_GATING,
    FIREWORKS_OPTION_LIST,
    FOREST_GATING_LIST,
    ITEM_QUALITY_LIST,
    KEEP_GATING,
    LEARNABLE_SPELL_LIST,
    MARRYMORE_GATING,
    MOLEVILLE_GATING,
    MONSTRO_GATING,
    PLAYABLE_CHARACTER_LIST,
    REGULAR_CHECKS,
    SEA_GATING,
    SEASIDE_BOSS_GATING,
    SHOP_QUALITY_LIST,
    SHUFFLED_BOSS_LIST,
    STARTER_CHARACTER_LIST,
    TEMPLE_GATING,
    TOWER_GATING,
    VAULT_GATING_LIST,
    VOLCANO_GATING,
    WIN_CONDITION_LIST,
)
from .enums import (
    AvailableMusic,
    BanditsWayGating,
    BarrelVolcanoGating,
    BelomeTempleGating,
    BoosterTowerGating,
    BossScaleOptions,
    BowsersKeepGating,
    EXPChallengeOptions,
    EXPMultiplierOptions,
    EquipmentCharactersOptions,
    EquipmentPropertiesOptions,
    FactoryGating,
    FireworksOptions,
    ForestMazeGating,
    ItemQualities,
    LearnableSpells,
    MarrymoreGating,
    Moleville1Gating,
    MonstroTownGating,
    PipeVaultGating,
    PlayableCharacters,
    SeaGating,
    ShopQualities,
    ShuffleLocationSelector,
    WinConditions,
    YaridovichGating,
)
from .types import (
    BooleanFlag,
    CategorizationFlag,
    NumberThresholdFlag,
    SelectOneFlag,
)

# ******** Party


class ShuffleCharacters(BooleanFlag):
    """Setting to randomize character order."""

    _id: str = "random"
    _name: str = "Randomize party recruitment order"
    _description: str = """If enabled, your characters will join your party in a random order.
<br>
<br>If disabled, you will start with Mario and recruit characters near their original locations."""


# if this is disabled, no starting/available options in this category can be changed


class StartingCharacter(SelectOneFlag):
    """Setting to choose your first character."""

    _id: str = "start"
    _name: str = "Starting Character"
    _description: str = (
        """The first character in your party, who will appear on your save menu."""
    )
    _optionEnum = PlayableCharacters
    _choices: List[PlayableCharacters] = STARTER_CHARACTER_LIST
    _default: PlayableCharacters = PlayableCharacters.MARIO


class PlayAsStarter(BooleanFlag):
    """Setting to make your overworld character reflect your first character."""

    _id: str = "allsprites"
    _name: str = "Play as starting character everywhere"
    _description: str = """If enabled, the character on your file select menu (also the character in your default 1st party position) will also be the character you play as outside of battle.
<br>
<br>If disabled, you will always play as Mario outside of battle, regardless of whether or not he is in your party."""


class StartingCharacters(NumberThresholdFlag):
    """Setting to choose the number of characters you start with."""

    _id: str = "size"
    # remember to set switch bit if > 3
    _name: str = "Starting party size"
    _description: str = (
        "The number of characters you will have already recruited at the start of the seed, including your starter."
    )
    _default: int = 1
    _min: int = 1
    _max: int = 5


class MaxCharacters(NumberThresholdFlag):
    """Setting to choose the max number of characters who can be recruited overall."""

    _id: str = "max"
    _name: str = "Maximum characters available"
    _description: str = """The maximum number of unique characters who can appear in the seed.
    <br>
    <br>There are no duplicate characters. If this number is higher than the amount of characters you have chosen in "Characters Allowed", then that number will be used instead."""
    _default: int = 5
    _min: int = 1
    _max: int = 5


class AvailableCharacters(CategorizationFlag):
    """Setting to choose which characters can be recruited in the seed."""

    _id: str = "avail"
    _name: str = "Characters allowed"
    _description: str = (
        """If a character is NOT highlighted (white text over blue), they will not appear in the seed. If they ARE highlighted, they may appear in the seed depending on your "Maximum characters available" setting."""
    )
    _optionEnum = PlayableCharacters
    _options: List[PlayableCharacters] = PLAYABLE_CHARACTER_LIST
    _enabled: List[PlayableCharacters] = PLAYABLE_CHARACTER_LIST


# ******** Equipment


class EquipmentCharacters(SelectOneFlag):
    """Setting to decide how characters are assigned to equipment."""

    _id: str = "perms"
    _name: str = "Equipment permissions"
    _description: str = """<b>Vanilla</b>: The list of characters who are permitted to equip each item remains unchanged from the original game.
<br>
<br><b>Vanilla, except anyone can wear any accessory</b>: Armor and weapon permissions are unchanged from the original game, but all accessories (including the Attack Scarf) can be equipped by anyone.
<br>
<br><b>Random, except anyone can wear any accessory</b>: Armor and weapon permissions are randomized, but all accessories can be equipped by anyone.
<br>
<br><b>Completely random</b>: All equips' permissions are randomized.
<br>
<br><b>Anyone can equip anything</b>: No equips are character-restricted."""
    _optionEnum = EquipmentCharactersOptions
    _choices: List[EquipmentCharactersOptions] = EQUIPMENT_CHARACTERS_LIST
    _default: EquipmentCharactersOptions = EquipmentCharactersOptions.VANILLA


class EquipmentProperties(SelectOneFlag):
    """Setting to decide how equipment stats are set"""

    _id: str = "stats"
    _name: str = "Equipment stats & buffs"
    _description: str = """<b>Default</b>: The stats and buffs on equipment are unchanged from the original game.
<br>
<br><b>Some buffs added</b>: The stats and buffs on equipment are mostly unchanged from the original game, except most armors are given one additional property (e.g. Fire Shirt nullifies damage from fire attacks). Additionally, some weapons will boost magic attack instead of physical attack.
<br>
<br><b>Completely random</b>: The stats and buffs on each piece of equipment is randomized."""
    _optionEnum = EquipmentPropertiesOptions
    _choices: List[EquipmentPropertiesOptions] = EQUIPMENT_PROPERTIES_LIST
    _default: EquipmentPropertiesOptions = EquipmentPropertiesOptions.VANILLA


class EquipmentNoSafety(BooleanFlag):
    """Setting to allow ridiculous rolls on equips."""

    _id: str = "unsafe"
    _name: str = "No Equipment Property Safety"
    _description: str = (
        "Normally, certain namesake items retain their protections: <b>Fearless Pin</b>, <b>Antidote Pin</b>, <b>Trueform Pin</b>, and <b>Wakeup Pin</b>. In addition, at least four equips will have OHKO protection. This flag removes those guarantees."
    )


class StarPieceHints(BooleanFlag):
    """Setting to make the Signal Ring hint toward star pieces."""

    _id: str = "hints"
    _name: str = "Signal Ring Star Piece hints"
    _description: str = """If enabled, the Signal Ring (if equipped to your active party) will play a sound when you enter a world area that contains a Star Piece.
<br>
<br>The Signal Ring will only sound off when you enter an area from the World Map, from loading a save, or from an area warp (ex: the Kero Sewers - Land's End pipe). Therefore, the chime does not necessarily indicate that your current room contains a Star Piece, but rather that at least one room in the area does."""


# ******** Stats & Spells


class EXPMultiplier(SelectOneFlag):
    """Setting to choose curve of enemy EXP"""

    _id: str = "exp"
    _name: str = "EXP multiplier"
    _description: str = (
        """If not set to "Default", all EXP gained will be doubled or tripled."""
    )
    _optionEnum = EXPMultiplierOptions
    _choices: List[EXPMultiplierOptions] = EXP_MULTIPLIER_OPTIONS
    _default: EXPMultiplierOptions = EXPMultiplierOptions.VANILLA


class CharacterStats(BooleanFlag):
    """Setting to randomize character stats and stat curves"""

    _id: str = "stats"
    _name: str = "Randomize character stats"
    _description: str = """If enabled, stats and stat curves for each playable character will be randomized. This also randomizes the number of FP you start with.
<br>
<br>If disabled, playable characters retain their original stats and stat curves."""


class CharacterLearnedSpells(BooleanFlag):
    """Setting to randomize which characters learn which spells"""

    _id: str = "spells"
    _name: str = "Randomize character learned spells"
    _description: str = (
        "The pool of spells learnable by each character will be randomized. This only covers spells originally learn-able by playable characters, and does not include enemy spells."
    )


class CharacterSpellStats(BooleanFlag):
    """Setting to randomize base power and FP of character spells"""

    _id: str = "spellstats"
    _name: str = "Randomize character spell stats"
    _description: str = (
        "The power and FP cost of character magic spells will be randomized."
    )


class CharacterSpellExtraElements(BooleanFlag):
    """Setting to assign elements to some element-neutral spells."""

    _id: str = "extraelements"
    _name: str = "Infuse more spells with elements"
    _description: str = """Geno Flash and Psych Bomb become Fire type spells.\n
Crusher and Bowser Crush become Earth (Jump) type spells.\n
Geno Beam becomes an Ice type spell."""


class CharacterSpellElements(BooleanFlag):
    """Setting to randomize the elements of elemental spells"""

    _id: str = "spellelements"
    _name: str = "Randomize character spell elements"
    _description: str = """Elemental party spells will be assigned a random element
 (i.e. Fire Orb may become Thunder Orb)."""


class UncapSuperJumps(BooleanFlag):
    """Setting to uncap super jumps (no longer maxes out at 100)"""

    # this needs testing
    _id: str = "uncap"
    _name: str = "Uncap Super Jumps"
    _description: str = "If enabled, you can do more than 100 Super Jumps at once."


class AvailableSpells(CategorizationFlag):
    """Setting to choose which spells can be learned"""

    _id: str = "avail"
    _name: str = "Available Player Spells"
    _description: str = """Highlighted (white text over blue) spells will be learned by at least one character. Spells that are not highlighted will not be learned by any character.
<br>
<br>Excluded spells are not replaced in characters' learnsets by other spells, so some characters will learn less than six total.
<br>
<br>Note: Excluding "Super Jump" may make some equips inaccessible depending on your other settings."""
    _optionEnum = LearnableSpells
    _options: List[LearnableSpells] = LEARNABLE_SPELL_LIST
    _enabled: List[LearnableSpells] = LEARNABLE_SPELL_LIST


# ******** Star Pieces


class ShuffleStarPieces(BooleanFlag):
    """Setting to randomize where star pieces are"""

    _id: str = "random"
    _name: str = "Randomize the locations of Star Pieces"
    _description: str = """If enabled, the Star Pieces may be found in places other than their original locations.
<br>
<br>If disabled, they will be rewarded by defeating the final bosses of Mushroom Kindom, Forest Maze, Moleville, Seaside Town, and Barrel Volcano, as well as a freestanding piece on Star Hill."""


# if this is disabled, no other options in this category can be changed


class TotalStarPieces(NumberThresholdFlag):
    """Setting to choose how many star pieces are in the seed"""

    _id: str = "avail"
    _name: str = "Total Star Pieces available"
    _description: str = (
        "The total number of Star Pieces (0-7) that can appear in the seed."
    )
    _default: int = 6
    _min: int = 0
    _max: int = 7


class EnabledBossChecks(CategorizationFlag):
    """Setting to decide which boss location can and cannot guard star pieces"""

    _id: str = "fights"
    _name: str = "Eligible Star Piece boss fight & mimic fight locations"
    _description: str = """If a check is highlighted (white text over blue), it is eligible to reward a Star Piece.
<br>
<br>If a check is not highlighted, it will still house a boss or mimic fight, but is guaranteed to not reward a Star Piece.
<br>
<br>Note: "Nimbus Land statue keeper" will always be the same fight as the enemy running through the final Nimbus Land hallway. You can fight either instance of this boss to get its star piece, but you will never get 2 star pieces from doing both copies of the fight."""
    _optionEnum = ShuffleLocationSelector
    _options: List[ShuffleLocationSelector] = BOSS_STAR_PIECE_LOCATIONS
    _enabled: List[ShuffleLocationSelector] = BOSS_STAR_PIECE_LOCATIONS


class StarPiecesRestrictedByArea(BooleanFlag):
    """Setting to make it so that each major world map section can only have 1 star piece"""

    _id: str = "restrict_map"
    _name: str = "Restrict number of Star Pieces in a World Map area"
    _description: str = """If enabled, each of the seven overworld map areas may only contain up to one Star Piece each.
<br>
<br>Note: This may not be respected if Bowser's Keep and Factory are both gated by 6 Star Pieces."""


# ******** Item shuffle


class ShuffleItems(BooleanFlag):
    """Setting to randomize retrievable items"""

    _id: str = "random"
    _name: str = "Randomize the contents of treasure chests and item rewards"
    _description: str = """If enabled, the contents of treasure chests, quest rewards, and (optionally) freestanding small items will be shuffled.
<br>
<br>If disabled, chests, quest rewards, and freestanding small items will remain unchanged from the original game."""


# if this is disabled, no options in this category can be changed


class ItemQuality(SelectOneFlag):
    """Setting to choose the quality guidelines of the randomized items"""

    _id: str = "quality"
    _name: str = """Item pool quality"""
    _description: str = """Restricts the incidence of certain items within the shuffled pool.
<br>
<br>If "Original item pool" is selected, items which only appear once in the original game will also not appear in unlimited shops. Additionally, two copies of the progressive Mystery Egg will be added to the pool, replacing some small items.
<br>
<br>If "Completely empty" is selected, any chest which does not contain a required item will be empty."""
    _optionEnum = ItemQualities
    _choices: List[ItemQualities] = ITEM_QUALITY_LIST
    _default: ItemQualities = ItemQualities.ORIGINAL


class BiasItemShuffle(BooleanFlag):
    """Setting to make better items harder to get"""

    _id: str = "bias"
    _name: str = "Bias better items to gated locations"
    _description: str = (
        """If enabled, harder-to-reach areas will generally house better items."""
    )


class NoStarEgg(BooleanFlag):
    """Setting to remove star egg from the pool"""

    _id: str = "noegg"
    _name: str = "No Star Egg"
    _description: str = (
        """If enabled, you will not find the Star Egg via any chests, overworld items, or NPC rewards."""
    )


class RestrictSpecialEquips(BooleanFlag):
    """Setting to make 10 special equips shuffled within each other"""

    _id: str = "restrict_monstro"
    _name: str = (
        'Shuffle "Special Item" exchange equips, Monstro Town reward equips, and postgame rewards'
    )
    _description: str = """If enabled, the FroggieStick, Chomp, Zoom Shoes, Attack Scarf, Super Suit, Quartz Charm, Jinx Belt, Ghost Medal, and both Lazy Shells will be shuffled within each other's original locations. This option ignores your chosen Item Quality setting.
<br>
<br>If 'Include postgame' is enabled, this pool will include the Sage Stick, Wonder Chomp, Stella 023, Enduring Brooch, E.ShinyStone, TeamworkBand, and CrystalShard. The Frying Pan will also be included in the pool so that every character's ultimate weapon is included.
<br>
<br>If disabled, the ten locations will simply contain random items, like every other item location."""


class RestrictSpecialEquipsExclusive(BooleanFlag):
    """Setting to make special equips ONLY available within their designated locations"""

    _id: str = "hard"
    _name: str = (
        'Exclude "Special Item" exchange equips & Monstro Town reward equips from all other locations'
    )
    _description: str = """If enabled alongside the "Shuffle 'Special Item exchange equips & Monstro Town reward equips" option, the ten items will ONLY appear at the ten designated locations, and nowhere else in the seed.
<br> 
<br>This option is redundant if you have selected "Original item pool" as your shuffle option.
<br>
<br>If disabled, these items can appear anywhere, subject to the restrictions of your chosen Item Pool Quality setting."""


class EXPStarsAnywhere(BooleanFlag):
    """Setting to allow almost any chest to be an EXP star chest"""

    _id: str = "xpstars"
    _name: str = "Shuffle EXP star chests"
    _description: str = """If enabled, the chests originally containing EXP stars will contain random checks. EXP stars may appear in any chest near monsters, unless your item pool is set to "Completely Empty".
<br>
<br>If disabled, EXP stars will be restricted to their original locations within Bandit's Way, Kero Sewers, Moleville Mines, Sea, Land's End, Nimbus Land, and Barrel Volcano."""


class MimicsAnywhere(BooleanFlag):
    """Setting to allow almost any chest to be a mimic chest"""

    _id: str = "mimics"
    _name: str = "Shuffle mimic chests"
    _description: str = """If enabled, any three chests in the world may be mimics. You will be able to run away from them, including fights initiated by failed slot machines. If you have "Scale boss stats to area difficulty" set to "Match to area", each mimic will be restricted to areas that are appropriate for its stats. However you should save often with this setting turned on, especially if item-hunting at the start of the seed.
<br>
<br>If disabled, mimic chests will remain in their original locations in Kero Sewers, Sunken Ship, and Bean Valley. You will not be able to run away from these fights, or from fights initiated by failed slot machines."""


class SlotsAnywhere(BooleanFlag):
    """Setting to allow almost any chest to be a slot machine chest"""

    _id: str = "slots"
    _name: str = "Shuffle slot machine chests"
    _description: str = """If enabled, the three slot machine chests in Bean Valley will contain random item checks. Random chests in the world can contain slot machines, unless your item pool is set to "Completely Empty".
<br>
<br>If disabled, the three original slot machines in Bean Valley will be unchanged.
<br>
<br>Note that a bad roll on a slot machine will initiate the third mimic chest fight. You can avoid this by timing your jumps to make the first two slots match, but be careful with this setting."""


class ShuffleBeetlemania(BooleanFlag):
    """Setting to turn gameboy kid into an item check, shuffling Beetlemania into the pool"""

    _id: str = "beetle"
    _name: str = "Shuffle Beetlemania"
    _description: str = (
        """If enabled, the Mushroom Kingdom inn kid will give you a random item check for 500 coins. Beetlemania will appear in a random location, unless your item pool is set to "Completely Empty"."""
    )


class ShuffleMagikoopaChest(BooleanFlag):
    """Setting to turn one random chest into an infinite coin chest, Magikoopa's chest becomes a random item"""

    _id: str = "kamek"
    _name: str = "Shuffle Magikoopa's coin chest"
    _description: str = (
        """If enabled, the chest in Magikoopa's room will contain a random item check. A random chest somewhere in the game will contain infinite coins, unless your item pool is set to "Completely Empty"."""
    )


class ShuffleWeddingGear(BooleanFlag):
    """Setting to shuffle the 4 wedding gear items anywhere in the world, all 4 must be found to fight the chapel boss"""

    _id: str = "marry"
    _name: str = "Shuffle Marrymore wedding gear"
    _description: str = """If enabled, the four pieces of wedding gear required to initiate the Marrymore boss fight will be located randomly within the world (not necessarily key item locations). Interacting with the four NPCs in the chapel will become item checks.
<br>
<br>If disabled, the Marrymore chapel minigame will behave as normal."""


class AnnoyingChests(BooleanFlag):
    """Setting to make empty chests perform the You Missed animation"""

    _id: str = "ym"
    _name: str = 'Empty chests should perform the "You Missed" animation'
    _description: str = (
        """If disabled, empty chests will simply appear as pre-opened."""
    )


class FireworksSetting(SelectOneFlag):
    """Setting to choose the fireworks trade quest behaviour"""

    _id: str = "fireworks"
    _name: str = """Fireworks trade sequence"""
    _description: str = """<b>Vanilla</b>: Unchanged from the original game.
<br>
<br><b>Shuffle Fireworks</b>: Fireworks is added to the "Special Item" pool, and the Fireworks shop becomes a "Special Item" location. The trading sequence is otherwise unchanged. If needed, you may get your Shiny Stone back from the shop girl after you have completed the trade sequence.
<br>
<br><b>Shuffle Progressive Fireworks</b>: One Fireworks, Shiny Stone, and Carbo Cookie are each shuffled somewhere completely random in the game, and you will always receive them in order. The Monstro Town sealed door is unlocked when you find the Shiny Stone.
<br>
<br>Note: If you do not have Bucket Warp enabled, completing the Carbo Cookie trade sequence will give you a random item if "Shuffle Fireworks" or "Shuffle Progressive Fireworks" is selected.
"""
    _optionEnum = FireworksOptions
    _choices: List[FireworksOptions] = FIREWORKS_OPTION_LIST
    _default: FireworksOptions = FireworksOptions.VANILLA


# ******** Progression availability


class KeyItemsAnywhere(BooleanFlag):
    """Setting to allow key items to be in any location besides a designated key item location"""

    _id: str = "keys_anywhere"
    _name: str = '"Special Items" can appear in the general item pool'
    _description: str = """If enabled, items belonging to your "Special Items" pocket can appear in any item location.
<br>
<br>If disabled, the "Special Items" will only be shuffled within each other's locations.
<br>
<br>The items targeted by this setting are the <b>Rare Frog Coin</b>, <b>Cricket Pie</b>, <b>Bambino Bomb</b>, <b>Castle Key 1</b>, <b>Castle Key 2</b>, <b>Alto Card</b>, <b>Tenor Card</b>, <b>Soprano Card</b>, <b>Greaper Flag</b>, <b>Dry Bones Flag</b>, <b>Big Boo Flag</b>, <b>Shed Key</b>, <b>Elder Key</b>, <b>Cricket Jam</b>, <b>Temple Key</b>, <b>Room Key</b>, <b>Seed</b>, and <b>Fertilizer</b> (and sometimes <b>Bright Card</b> and <b>Fireworks</b>)."""


class StarPieceAvailability(BooleanFlag):
    """Setting to allow star pieces to be in any location instead of only guarded by bosses"""

    _id: str = "stars_anywhere"
    _name: str = "Star Pieces can appear in the general item pool"
    _description: str = (
        "If enabled, some Star Pieces may be shuffled in with items instead of being only granted by boss fights."
    )


# disable this setting if empty chests is turned on. Doesn't make sense to hunt down a check with no confirmation that you've found it
class InvisibleFlagsSetting(BooleanFlag):
    """Setting to place the three invisible items somewhere random in the world"""

    _id: str = "moveflags"
    _name: str = "Move invisible flag checks"
    _description: str = """Chooses where the invisible items placed by the Three Musty Fears are located.
<br>
<br>If not enabled, these checks will remain in their default locations (Mario's Pad bed, Rose Town sign, Yo'ster Isle goalpost).
<br>
<br>If enabled, the three checks will be located somewhere random in the world as an invisible item. The Three Musty Fears will give you hints as to their locations."""


class RemakePostgame(BooleanFlag):
    """Setting to include "demake" postgame content from the SMRPG remake"""

    _id: str = "postgame"
    _name: str = "Include remake content"
    _description: str = """If enabled, some content exclusive to the 2023 Switch remake will be included:
<ol>
<li>All seven postgame fights</li>
<li>All postgame-exclusive items</li>
<li>Extra prizes in Mushroom Way and Land's End</li>
</ol>"""


class EnabledRegularChecks(CategorizationFlag):
    """Setting to choose which locations can and cannot contain progression"""

    _id: str = "chests"
    _name: str = "General item pool checks"
    _description: str = """If a check is highlighted (white text over blue), it is eligible to contain items required to complete the seed.
<br>
<br>If a check is not highlighted, its contents will still be shuffled, but it will not contain any items required to complete the seed.
<br>
<br>This setting only applies if you have "Special Items can appear in the general item pool" or "Star Pieces can appear in the general item pool" enabled."""
    _optionEnum = ShuffleLocationSelector
    _options: List[ShuffleLocationSelector] = REGULAR_CHECKS
    _enabled: List[ShuffleLocationSelector] = REGULAR_CHECKS


# ******** Item behaviour


class ReplaceItems(BooleanFlag):
    """Setting to replace bad items with coins"""

    _id: str = "replace"
    _name: str = "Replace some chest items with coins"
    _description: str = (
        "If enabled, the worst items (Wilt Shrooms, etc) will sometimes be replaced with coins in chests."
    )


class QuickHitCoins(BooleanFlag):
    """Setting to make coin chests grant all coins in one hit"""

    _id: str = "quick"
    _name: str = "Quick-hit coin chests"
    _description: str = (
        "If enabled, all coin and frog coin chests will grant coins in a single hit instead of multiple hits. (Normally, only chests in room which graphically cannot load coins will at this way.)"
    )


class PoisonMushroom(BooleanFlag):
    """Setting to randomize the effect of the poison mushroom"""

    _id: str = "fake"
    _name: str = "Change Fake Mushroom's Effect"
    _description: str = (
        "Randomize the status effect inflicted on a party member with the Fake Mushroom. It will only give "
        "one status effect per seed, which has a 1/8 chance of being Invincibility."
    )


class EXPChallenge(SelectOneFlag):
    """Setting to make EXP star values conditional on certain completed quests"""

    _id: str = "xpstar"
    _name: str = "EXP Star Behaviour"
    _description: str = """<b>Default</b>: EXP stars can give you 1 to 11 EXP per hit as normal.
<br>
<br><b>Star Pieces (easy/hard)</b>: EXP per star increases with the number of Star Pieces collected. This is not adjusted for lower max Star Piece counts.
<br>
<br><b>Bosses (easy/hard)</b>: EXP per star increases with the number of bosses you have defeated.
<br>
<br><b>No EXP</b>: EXP stars give you 0 EXP.
<br>
<br>"Easy" settings grant 2, 4, 5, 6, 8, 9, or 11 EXP depending on your progress, and "Hard" settings grant 1, 2, 3, 5, 6, 7, or 11 EXP."""
    _optionEnum = EXPChallengeOptions
    _choices: List[EXPChallengeOptions] = EXP_CHALLENGE_OPTIONS_LIST
    _default: EXPChallengeOptions = EXPChallengeOptions.VANILLA


class GrateGuyPrizeThreshold(NumberThresholdFlag):
    """Setting to modify how many wins needed for casino prize"""

    _id: str = "gg"
    _name: str = 'Required "Look The Other Way" wins'
    _description: str = (
        "The number of times required to win Grate Guy's casino minigame to receive its ultimate prize."
    )
    _default: int = 100
    _min: int = 1
    _max: int = 255


class KnifeGuyPrizeThreshold(NumberThresholdFlag):
    """Setting to modify how many wins needed for knife guy prize"""

    _id: str = "kg"
    _name: str = "Required juggling wins"
    _description: str = (
        "The number of wins minus losses required to win Knife Guy's ultimate juggling game prize."
    )
    _default: int = 12
    _min: int = 1
    _max: int = 254


class SuitePrize1Threshold(NumberThresholdFlag):
    """Setting to modify how many sleeps needed for 1st marrymore gift"""

    _id: str = "s1"
    _name: str = "Required Suite prize #1 stays"
    _description: str = (
        "The number of times required to stay in the Marrymore Suite to receive the first special gift"
    )
    _default: int = 1
    _min: int = 1
    _max: int = 254


class SuitePrize2Threshold(NumberThresholdFlag):
    """Setting to modify how many sleeps needed for 2nd marrymore gift"""

    _id: str = "s2"
    _name: str = "Required Suite prize #2 stays"
    _description: str = (
        "The number of times required to stay in the Marrymore Suite to receive the second special gift"
    )
    _default: int = 3
    _min: int = 1
    _max: int = 254


class SuitePrize3Threshold(NumberThresholdFlag):
    """Setting to modify how many sleeps needed for 3rd marrymore gift"""

    _id: str = "s3"
    _name: str = "Required Suite prize #3 stays"
    _description: str = (
        "The number of times required to stay in the Marrymore Suite to receive the third special gift"
    )
    _default: int = 5
    _min: int = 1
    _max: int = 254


class SuitePrize4Threshold(NumberThresholdFlag):
    """Setting to modify how many sleeps needed for 4th marrymore gift"""

    _id: str = "s4"
    _name: str = "Required Suite prize #4 stays"
    _description: str = (
        "The number of times required to stay in the Marrymore Suite to receive the fourth special gift"
    )
    _default: int = 10
    _min: int = 1
    _max: int = 254


class SuitePrize5Threshold(NumberThresholdFlag):
    """Setting to modify how many sleeps needed for 5th marrymore gift"""

    _id: str = "s5"
    _name: str = "Required Suite prize #5 stays"
    _description: str = (
        "The number of times required to stay in the Marrymore Suite to receive the fifth special gift"
    )
    _default: int = 15
    _min: int = 1
    _max: int = 254


class SuitePrize6Threshold(NumberThresholdFlag):
    """Setting to modify how many sleeps needed for 6th marrymore gift"""

    _id: str = "s6"
    _name: str = "Required Suite prize #6 stays"
    _description: str = (
        "The number of times required to stay in the Marrymore Suite to receive the sixth special gift"
    )
    _default: int = 200
    _min: int = 1
    _max: int = 254


class SuperJump1Threshold(NumberThresholdFlag):
    """Setting to modify how many super jumps needed for 1st prize"""

    _id: str = "sj1"
    _name: str = "Required Super Jumps for prize #1"
    _description: str = (
        "The number of consecutive Super Jumps required for the first prize in Monstro Town"
    )
    _default: int = 30
    _min: int = 1
    _max: int = 99


class SuperJump2Threshold(NumberThresholdFlag):
    """Setting to modify how many super jumps needed for 2nd prize"""

    _id: str = "sj2"
    _name: str = "Required Super Jumps for prize #2"
    _description: str = (
        "The number of consecutive Super Jumps required for the second prize in Monstro Town"
    )
    _default: int = 100
    _min: int = 2
    _max: int = 100


# ******** Area Access


class BanditsWayGate(SelectOneFlag):
    """Setting to choose how to open Bandit's Way"""

    _id: str = "bw"
    _name: str = """Bandit's Way access"""
    _description: str = """<b>Recruit Mallow</b>: Bandit's Way will become available on the world map when Mallow joins the party.
<br>
<br><b>Finish Mushroom Way</b>: Bandit's Way will become available on the world map when you defeat the boss of Mushroom Way.
<br>
<br><b>Defeat Hammer Bros</b>: Bandit's Way will become available on the world map when you have found and defeated the Hammer Bros boss battle.
<br>
<br><b>Always Open</b>: Bandit's Way will be available on the world map from the start of the game."""
    _optionEnum = BanditsWayGating
    _choices: List[BanditsWayGating] = BANDITS_WAY_GATING_LIST
    _default: BanditsWayGating = BanditsWayGating.MALLOW


class ForestMazeGate(SelectOneFlag):
    """Setting to choose how to open Forest Maze"""

    _id: str = "fm"
    _name: str = """Forest Maze access"""
    _description: str = """<b>Find Geno</b>: Forest Maze will become available on the world map when you first see Geno. "See" does not necessarily mean "recruit".
<br>
<br><b>Exchange Cricket Pie</b>: Forest Maze will become available on the world map when you turn in the Cricket Pie to Frogfucius.
<br>
<br><b>Always Open</b>: Forest Maze will be available on the world map from the start of the game."""
    _optionEnum = ForestMazeGating
    _choices: List[ForestMazeGating] = FOREST_GATING_LIST
    _default: ForestMazeGating = ForestMazeGating.GENO


class PipeVaultGate(SelectOneFlag):
    """Setting to choose how to open Pipe Vault"""

    _id: str = "pv"
    _name: str = """Pipe Vault access"""
    _description: str = """<b>Recruit Geno</b>: Pipe Vault will be unblocked when Geno joins the party.
<br>
<br><b>Finish Forest Maze</b>: Pipe Vault will be unblocked when you defeat the final boss of Forest Maze.
<br>
<br><b>Defeat Bowyer</b>: Pipe Vault will be unblocked when you have found and defeated the Bowyer boss battle.
<br>
<br><b>Always Open</b>: Pipe Vault will be unblocked from the start of the game."""
    _optionEnum = PipeVaultGating
    _choices: List[PipeVaultGating] = VAULT_GATING_LIST
    _default: PipeVaultGating = PipeVaultGating.OPEN


class Moleville1Gate(SelectOneFlag):
    """Setting to choose how to open Moleville Mines"""

    _id: str = "me"
    _name: str = """Moleville Mines entrance access"""
    _description: str = """<b>Recruit Geno</b>: The top door inside the Moleville Mines entrance will be accessible when Geno joins the party.
<br>
<br><b>Finish Forest Maze</b>: The top door inside the Moleville Mines entrance will be accessible when you defeat the final boss of Forest Maze.
<br>
<br><b>Defeat Bowyer</b>: The top door inside the Moleville Mines entrance will be accessible when you have found and defeated the Bowyer boss battle.
<br>
<br><b>Always Open</b>: The top door inside the Moleville Mines entrance will be accessible from the start of the game."""
    _optionEnum = Moleville1Gating
    _choices: List[Moleville1Gating] = MOLEVILLE_GATING
    _default: Moleville1Gating = Moleville1Gating.OPEN


class BoosterTowerGate(SelectOneFlag):
    """Setting to choose how to open Booster Tower"""

    _id: str = "bt"
    _name: str = """Booster Tower access"""
    _description: str = """<b>Recruit character</b>: Booster Tower's door can be unlocked when you recruit the selected character.
<br>
<br><b>Finish Moleville</b>: Booster Tower's door will unlock when you defeat the final boss of Moleville.
<br>
<br><b>Defeat Punchinello</b>: Booster Tower's door will unlock when you have found and defeated the Punchinello boss battle.
<br>
<br><b>Always Open</b>: Booster Tower's door will be unlocked from the start of the game."""
    _optionEnum = BoosterTowerGating
    _choices: List[BoosterTowerGating] = TOWER_GATING
    _default: BoosterTowerGating = BoosterTowerGating.BOWSER


class MarrymoreGate(SelectOneFlag):
    """Setting to choose how to open Marrymore back door"""

    _id: str = "mm"
    _name: str = """Marrymore back door access"""
    _description: str = """<b>Finish Booster Hill</b>: The chapel back door will open when you complete Booster Hill one time.
<br>
<br><b>Finish Booster Tower</b>: The chapel back door will open when you defeat the balcony boss of Booster Tower.
<br>
<br><b>Defeat Knife Guy & Grate Guy</b>: The chapel back door will open when you have found and defeated the Knife Guy & Grate Guy boss battle.
<br>
<br><b>Always Open</b>: The chapel back door will be open from the start of the game."""
    _optionEnum = MarrymoreGating
    _choices: List[MarrymoreGating] = MARRYMORE_GATING
    _default: MarrymoreGating = MarrymoreGating.HILL


class SeaGate(SelectOneFlag):
    """Setting to choose how to open Sea"""

    _id: str = "sea"
    _name: str = """Sea & Sunken Ship access"""
    _description: str = """<b>Recruit Toadstool</b>: The Sea will become available on the world map when Toadstool joins the party.
<br>
<br><b>Collect 4 Star Pieces</b>: The Sea will become available on the world map when you collect 4 Star Pieces.
<br>
<br><b>Defeat Bundt</b>: The Sea will become available on the world map when you have found and defeated the Bundt boss battle.
<br>
<br><b>Always Open</b>: The Sea & Sunken Ship will be available on the world map from the start of the game."""
    _optionEnum = SeaGating
    _choices: List[SeaGating] = SEA_GATING
    _default: SeaGating = SeaGating.STAR_4


class BelomeTempleGate(SelectOneFlag):
    """Setting to choose how to open Belome Temple"""

    _id: str = "tmpl"
    _name: str = """Belome Temple access"""
    _description: str = """<b>Finish Seaside Town</b>: The first Fortune Teller shaman will not appear until you have defeated the boss of Seaside Town.
<br>
<br><b>Defeat Yaridovich</b>: The first Fortune Teller shaman will appear when you have found and defeated the Yaridovich boss battle.
<br>
<br><b>Always Open</b>: Belome Temple access is unrestricted."""
    _optionEnum = BelomeTempleGating
    _choices: List[BelomeTempleGating] = TEMPLE_GATING
    _default: BelomeTempleGating = BelomeTempleGating.OPEN


class MonstroTownGate(SelectOneFlag):
    """Setting to choose how to open Monstro Town"""

    _id: str = "mt"
    _name: str = """Monstro Town access"""
    _description: str = """<b>Finish Land's End</b>: Monstro Town will become available on the World Map once you take the pipe behind the boss of Belome Temple.
<br>
<br><b>Defeat Belome 2</b>: Monstro Town will become available on the World Map when you have found and defeated the Belome 2 boss battle. The pipe in Land's End will be blocked until this happens.
<br>
<br><b>Always Open</b>: Monstro Town will be available on the World Map from the start of the game."""
    _optionEnum = MonstroTownGating
    _choices: List[MonstroTownGating] = MONSTRO_GATING
    _default: MonstroTownGating = MonstroTownGating.LANDS_END


class BarrelVolcanoGate(SelectOneFlag):
    """Setting to choose how to open Barrel Volcano"""

    _id: str = "bv"
    _name: str = """Barrel Volcano access"""
    _description: str = """<b>Finish Nimbus Land</b>: Barrel Volcano will become available on the World Map once you defeat the final boss of Nimbus Castle.
<br>
<br><b>Defeat Valentina</b>: Barrel Volcano will become available on the World Map when you have found and defeated the Valentina boss battle.
<br>
<br><b>Always Open</b>: Barrel Volcano will be available on the World Map from the start of the game."""
    _optionEnum = BarrelVolcanoGating
    _choices: List[BarrelVolcanoGating] = VOLCANO_GATING
    _default: BarrelVolcanoGating = BarrelVolcanoGating.NIMBUS


class BowsersKeepGate(SelectOneFlag):
    """Setting to choose how to open Bowser's Keep"""

    _id: str = "bk"
    _name: str = """Bowser's Keep access"""
    _description: str = """<b>Collect 6 Star Pieces</b>: Bowser's Keep will become available on the world map when you collect 6 Star Pieces.
<br>
<br><b>Finish Barrel Volcano</b>: Bowser's Keep will become available on the World Map once you defeat the final boss of Barrel Volcano.
<br>
<br><b>Defeat Axem Rangers</b>: Bowser's Keep will become available on the World Map when you have found and defeated the Axem Rangers boss battle.
<br>
<br><b>Always Open</b>: Bowser's Keep will be available on the world map from the start of the game."""
    _optionEnum = BowsersKeepGating
    _choices: List[BowsersKeepGating] = KEEP_GATING
    _default: BowsersKeepGating = BowsersKeepGating.VOLCANO


class FactoryGate(SelectOneFlag):
    """Setting to choose how to open Outer Factory"""

    _id: str = "wf"
    _name: str = """Factory access"""
    _description: str = """<b>Open when Bowser's Keep is opened</b>: When Bowser's Keep becomes available on the world map, Factory will also be immediately available on the world map.
<br>
<br><b>Finish Bowser's Keep</b>: Factory will become available on the world map when you complete Bowser's Keep for the first time.
<br>
<br><b>Defeat Exor</b>: Factory will become available on the World Map when you have found and defeated the Exor boss battle and Bowser's Keep has been opened.
<br>
<br><b>Collect 6 Star Pieces</b>: Factory will become available on the world map when you collect 6 Star Pieces and Bowser's Keep has been opened."""
    _optionEnum = FactoryGating
    _choices: List[FactoryGating] = FACTORY_GATING
    _default: FactoryGating = FactoryGating.KEEP


# ******** Boss & Endgame Access


class YaridovichGate(SelectOneFlag):
    """Setting to choose how to open Seaside Town boss fight"""

    _id: str = "seaside"
    _name: str = """Seaside boss fight access"""
    _description: str = """<b>Finish Sunken Ship</b>: The Seaside boss fight will become available after you defeat the final boss of Sunken Ship.
<br>
<br><b>Defeat Johnny</b>: The Seaside boss fight will become available after you find and defeat the Johnny boss fight.
<br>
<br><b>Always Open</b>: The Seaside boss will be available from the start of the game."""
    _optionEnum = YaridovichGating
    _choices: List[YaridovichGating] = SEASIDE_BOSS_GATING
    _default: YaridovichGating = YaridovichGating.SHIP


class SkipMustyFearsSequence(BooleanFlag):
    """Setting to skip needing to talk to the 3 Musty Fears to place invisible items"""

    _id: str = "skip_musty"
    _name: str = "Skip 3 Musty Fears sequence"
    _description: str = """This flag affects the Musty Fears checks (normally Mario's Pad bed, Rose Town sign, and Yo'ster Isle goalpost; or whichever three locations are added to the seed when "Move invisible flag checks" is set).
<br>
<br>If disabled, the affected checks will become available after you visit the Musty Fears Inn in Monstro Town.
<br>
<br>If enabled, the affected checks will be available from the start of the seed."""


class BowserDoorRequirements(NumberThresholdFlag):
    """Setting to choose how many doors are required in bowser's keep"""

    _id: str = "doors"
    _name: str = "Required Bowser's Keep obstacle doors"
    _description: str = (
        "The number of doors required to progress through Bowser's Keep."
    )
    _default: int = 4
    _min: int = 1
    _max: int = 6


class StarPiecesRequired(NumberThresholdFlag):
    """Setting to choose how many star pieces allow you to fight the factory final boss"""

    _id: str = "endgame"
    _name: str = "Star Pieces required to access the final Factory boss"
    _description: str = (
        "The total number of Star Pieces (0-7) that are required to access the final boss. Cannot be higher than Total Star Pieces."
    )
    _default: int = 6
    _min: int = 0
    _max: int = 7


class CasinoWarp(BooleanFlag):
    """Setting to allow you to warp to the final factory boss from the casino"""

    _id: str = "cwarp"
    _name: str = "Casino Warp"
    _description: str = (
        """If enabled, a trampoline warping directly to the final boss will become available in Grate Guy's Casino once you have collected the number of Star Pieces specified in 'Star Pieces required to beat the game'."""
    )


class BucketWarp(BooleanFlag):
    """Setting to allow you to warp to the final factory boss from the moleville frog coin bucket"""

    _id: str = "bwarp"
    _name: str = "Bucket Warp"
    _description: str = (
        "If enabled, trading a Carbo Cookie to the bucket girl in Moleville will reveal a warp to the final boss once you have collected the number of Star Pieces specified in 'Star Pieces required to beat the game'."
    )


class FastTravel(BooleanFlag):
    """Setting that enables shortcut exits out of inner factory and booster tower"""

    _id: str = "fasttravel"
    _name: str = "Fast travel"
    _description: str = """If enabled, the following changes will be applied to the game:
<ol>
<li>Traveling to the top of Booster Tower after defeating the balcony boss will always warp you to the ground.</li>
<li>Reaching the Inner Factory will reveal a trampoline that warps you to the world map.</li>
<li>Reaching the Inner Factory will enable a world map shortcut that places you in Inner Factory.</li>
</ol>"""


class WinCondition(SelectOneFlag):
    """Setting to choose what ends the game"""

    _id: str = "objective"
    _name: str = "Condition required to beat the game"
    _description: str = """<b>Beat the Factory</b>: When you collect the number of Star Pieces specified in your 'Star Pieces required to access the final Factory boss' setting, the button in the Inner Factory (as well as any enabled warps) will be enabled to allow you to access the final boss and beat the game.
<br>
<br><b>Beat Smithy</b>: The game is over as soon as you find Smithy and defeat him. (If you don't have him shuffled into the boss pool, this is effectively the same thing as "Beat the Factory".)
<br>
<br><b>Collect required Star Pieces</b>: When you collect the number of Star Pieces specified in your 'Star Pieces required to access the final Factory boss' setting, the game is over and the credits will roll.
<br>
<br><b>Beat Monstro Town sealed door</b>: The game is over when you defeat the boss behind the sealed door in Monstro Town, regardless of your Star Piece count."""
    _optionEnum = WinConditions
    _choices: List[WinConditions] = WIN_CONDITION_LIST
    _default: WinConditions = WinConditions.FACTORY


# ******** Puzzles


class BallSolitaireShuffle(BooleanFlag):
    """Setting to randomize the ball solitaire starting pattern"""

    _id: str = "ball"
    _name: str = "Randomize Ball Solitaire"
    _description: str = "The layout for the Ball Solitaire minigame will be randomized."


class MagicButtonShuffle(BooleanFlag):
    """Setting to randomize the green button game starting pattern"""

    _id: str = "button"
    _name: str = "Randomize Magic Buttons"
    _description: str = "The layout for the Magic Buttons minigame will be randomized."


class QuizShuffle(BooleanFlag):
    """Setting to randomize the quiz questions"""

    _id: str = "quiz"
    _name: str = "Randomize Dr. Topper Quiz"
    _description: str = (
        "The question pool for the Dr. Topper quiz will include new questions provided by the community."
    )


class RandomTadpolePondSong(BooleanFlag):
    """Setting to randomize the tadpole pond songs"""

    _id: str = "melody"
    _name: str = "Randomize Tadpole Pond songs"
    _description: str = (
        """If enabled, the songs required for the three Tadpole Pond songs will be selected from a random pool, submitted by players. Hints will be available in their normal locations within Tadpole Pond, Moleville Mines, and Monstro Town."""
    )


class RandomSunkenShipPassword(BooleanFlag):
    """Setting to randomize the ship password"""

    _id: str = "pwd"
    _name: str = "Randomize Sunken Ship password"
    _description: str = """If enabled, the password for the Sunken Ship will be changed. Hints are available in the 6 ship puzzles, and occasionally on posted notes within the Sunken Ship.
<br/>
<br/><b>Be warned that some of these are very difficult, or may be references to things you aren't familiar with.</b> The nearby shop shaman will tell you how many of your letters were correct when you submit an incorrect password."""


class BowserDoorShuffle(BooleanFlag):
    """Setting to randomize the room order of the six red door hallways"""

    _id: str = "doors"
    _name: str = "Randomize Bowser's Keep room sequences"
    _description: str = (
        """If enabled, the 18 rooms making up the six Bowser's Keep obstacle course doors will be shuffled into six random sequences of three rooms each."""
    )


class SkipMinecart(BooleanFlag):
    """Setting to skip mandatory minecart"""

    _id: str = "skipcart"
    _name: str = "Skip Minecart minigame"
    _description: str = (
        """If enabled, boarding the minecart for the first time will teleport you back to Moleville. Subsequent visits to the minecart room will play the minigame as normal."""
    )


class BetterTips(BooleanFlag):
    """Setting to offer better items from repeatable quests"""

    _id: str = "rng"
    _name: str = "Better Event RNG"
    _description: str = """If enabled, the following changes will take effect:
<br/>
<br/>Some repeatable item grants will give a better, or wider, variety of items. Example of this include Knife Guy's juggling game junk prizes, or tips from working in the Marrymore hotel. This setting has no impact on singular, clearable item checks.
<br/>
<br/>Your odds on Mushroom Boy's prizes and the Mushroom Derby cookie bet races will be improved.
<br/>
<br/>The cloud miniboss in Land's End will have an increased spawn rate. 
<br/>
<br/>Forest Maze mushrooms may be ANY kind of mushroom, regardless of your max item quality settings.
    """


# ******** Shops


class ShuffleShops(BooleanFlag):
    """Setting to randomize shop contents"""

    _id: str = "random"
    _name: str = "Randomize the contents of shops"
    _description: str = (
        """If enabled, the contents of all regular shops and Frog Coin shops (including the Moleville treasure shop, Marrymore Suite room service menu, and Moleville swap shop) will be randomized."""
    )


# if this is disabled, no options in this category can be changed


class ShopQuality(SelectOneFlag):
    """Setting to choose guidelines for shop quality"""

    _id: str = "quality"
    _name: str = """Shop contents quality"""
    _description: str = """Restricts the incidence of certain items in shops.
<br>
<br>"Completely random" means that some items which originally did not appear in shops may now appear in shops, but only a small pool of items are guaranteed to appear. Some items will never appear in non-depletable shops. 
<br>
<br>If "Completely empty" is selected, all shops will be disabled."""
    _optionEnum = ShopQualities
    _choices: List[ShopQualities] = SHOP_QUALITY_LIST  # maybe just o for o
    _default: ShopQualities = ShopQualities.ORIGINAL


class BiasShopShuffle(BooleanFlag):
    """Setting to make better items in shops that are harder to access"""

    _id: str = "bias"
    _name: str = "Bias better items to gated shops"
    _description: str = (
        """If enabled, harder-to-reach shops will generally sell better items."""
    )


class NoPickMeUps(BooleanFlag):
    """Setting to remove revives from item pool"""

    _id: str = "nolife"
    _name: str = "Exclude Pick Me Ups"
    _description: str = """If enabled, Pick Me Ups will not be sold in any shops."""


class ShowEquips(BooleanFlag):
    """Setting to show who can wear an equip, even chars you havent recruited"""

    _id: str = "showperms"
    _name: str = "Always show all permitted characters on equips"
    _description: str = "Always show who can equip what in stores."


class FreeShops(BooleanFlag):
    """Setting to make all shops free"""

    _id: str = "free"
    _name: str = "'Free' Shops"
    _description: str = (
        """If enabled, all shop items will cost 1 coin. You will start with 9999 coins and 999 frog coins."""
    )


# ******** Enemies & Bosses


class BossShuffle(BooleanFlag):
    """Setting to randomize which bosses are in which positions"""

    _id: str = "random"
    _name: str = "Randomize boss positions"
    _description: str = (
        "If enabled, the positions of bosses (including Pandorite, Hidon, Box Boy, Chester, and Mokura) are shuffled."
    )

    # if false, disable stat scaling and mimics anywhere


class BossShuffleScaleStats(SelectOneFlag):
    """Setting to make bosses inherit the stats of their locations"""

    _id: str = "scale"
    _name: str = "Scale boss stats"
    _description: str = """<b>Do not scale</b>: Boss fights retain their relative original stats, regardless of where they are placed. For example, Culex would still have around 4000 HP, even if he's in Mushroom Way.
<br>
<br><b>Match to area</b>: A boss fight that has been shuffled into a different area will have its stats scaled to match the area's original boss. For example, Culex would have about 100 HP if he's in Mushroom Way.
<br>
<br><b>Completely random</b>: A boss fight will inherit the relative stats of a random other location, regardless of position. For example, Culex could be placed in Mushroom Way, but have 1200 HP because he's inherited Belome 2's original stats."""
    _optionEnum = BossScaleOptions
    _choices: List[BossScaleOptions] = BOSS_SCALE_LIST
    _default: BossScaleOptions = BossScaleOptions.VANILLA


class SafeLogicProgression(BooleanFlag):
    """Setting to not require lategame bosses to be defeated before earlier bosses that will have given enough exp for it"""

    _id: str = "safe_prog"
    _name: str = """Remove boss progression safety"""
    _description: str = """Normally, the randomizer's logic will not expect you to defeat lategame boss locations before you can at least beat some earlygame boss locations. This check removes this safety.
<br>
<br>This check is redundant if "Scale boss stats" is not set to "Match to area"."""


class BossReplaceMinigameSprites(BooleanFlag):
    """Setting to include Dodo minigame, booster hill, and ship pirate battles to be affected by boss shuffle"""

    _id: str = "allsprites"
    _name: str = "Replace important NPCs to match shuffled bosses"
    _description: str = """If enabled: All sprites related to an area boss will be changed to match the shuffled positions of bosses.
<br>
<br>If disabled: Some sprites will be left unchanged from the original game to accommodate visual cues (such as the Booster Hill snifits, or Dodo in his statue room) or progression knowledge on required sub-fights (such as the Bandana Reds in Sunken Ship)."""


class DifferentiateRepeatedBosses(BooleanFlag):
    """Setting to make similar-looking bosses be coloured slightly differently"""

    _id: str = "diff"
    _name: str = "Differentiate similar bosses"
    _description: str = """If enabled, Croco, Jinx, Belome, and the four mimics' different iterations will look slightly different in the overworld (battle sprites remain unchanged).
<br>
<br>Croco 2 will have a darker hat.
<br>
<br>Jinx 2/3/4's hair will be black/white/blue respectively.
<br>
<br>Belome 2 will be more subdued, and coloured like the golden Belome statue. Belome 3 will have purple highlights instead of red.
<br>
<br>Pandorite will be tinted orange, Hidon will be tinted green, and Chester will be tinted purple.
<br>
<br>Punchinello2 will have a darker hat.
<br>
<br>Duel Johnny will be red instead of blue.
<br>
<br>Fancy Bundt will have a purple raspberry instead of red.
<br>
<br>Booster 023 will have a darker shirt.
<br>
<br>Culex 3D will have green crystals instead of blue."""


class ShuffledBosses(CategorizationFlag):
    """Setting to exclude certain bosses from being shuffled to another location"""

    _id: str = "pool"
    _name: str = "Shuffled boss fights"
    _description: str = """If a boss is highlighted (white text over blue), it will be shuffled into a pool and placed in a random boss location.
<br>
<br>If a boss is not highlighted, it will stay in its original location."""
    _optionEnum = BossLocations
    _options: List[BossLocations] = SHUFFLED_BOSS_LIST
    _enabled: List[BossLocations] = SHUFFLED_BOSS_LIST


class EnemyStats(BooleanFlag):
    """Setting to randomize enemy stats"""

    _id: str = "stats"
    _name: str = "Randomize enemy stats"
    _description: str = """If enabled, enemy stats and immunities/weaknesses will be randomized.
<br>
<br>If disabled, enemies retain their original stats (subject to placement shuffling, if enabled), immunities, and vulnerabilities."""


class EnemyDrops(BooleanFlag):
    """Setting to randomize enemy battle drops"""

    _id: str = "drops"
    _name: str = "Randomize enemy drops"
    _description: str = (
        "If enabled, the EXP and in-battle items received from battles will be randomized."
    )


class EnemyFormations(BooleanFlag):
    """Setting to randomize the formations of enemies in a battle"""

    _id: str = "formations"
    _name: str = "Randomize formations"
    _description: str = (
        "If enabled, enemy encounters may contain random unexpected additional enemies and be laid out erratically. Boss formations are not affected."
    )


class EnemyAttacks(BooleanFlag):
    """Setting to randomize the attacks that enemies can cast, and their effects"""

    _id: str = "attacks"
    _name: str = "Randomize attack stats and effects"
    _description: str = (
        "If enabled, enemy spells and attacks will have their power randomized. Attacks which cast statuses will have the status effects randomized, and attacks which normally don't inflict statuses may inflict unexpected statuses."
    )


class EnemyNoSafetyChecks(BooleanFlag):
    """Setting to remove checks and balances for enemy shuffling."""

    _id: str = "unsafe"
    _name: str = "No safety checks"
    _description: str = (
        "If enabled, removes safety checks on enemy attack shuffle that prevent abnormally large effects."
    )


class EnemySpells(BooleanFlag):
    """Setting to randomize the spells that enemies can cast"""

    _id: str = "spells"
    _name: str = "Randomize enemy spell assignments"
    _description: str = (
        "If enabled, enemies can cast random spells. I.E. Mack could cast Blast instead of Flame."
    )


class ExperienceNoRegular(BooleanFlag):
    """Setting to make regular enemies give no EXP"""

    _id: str = "noregexp"
    _name: str = "Remove EXP from regular enemy encounters"


class ExperienceNoBosses(BooleanFlag):
    """Setting to make bosses give no EXP"""

    _id: str = "nobossexp"
    _name: str = "Remove EXP from boss encounters"


class RequireBossFights(BooleanFlag):
    """Setting to disable all alternate boss fight win conditions"""

    _id: str = "noskips"
    _name: str = "Disable all alternate boss fight win conditions"
    _description: str = """If set, the following actions will NOT grant you a Star Piece or open any related map locations, and you must fight the associated boss in order to retrieve their Star Piece (if they have one) and unlock their associated map area (if they unlock one):
<ul>
<li> Performing Mack Skip (the Chancellor will not advance the script)</li>
<li> Completing the Booster Tower curtain minigame (a copy of the boss will appear in the room corner)</li>
<li> Completing the Nimbus Castle statue minigame, or eliminating the boss in the final hallway with an EXP star (a copy of the boss will appear in the nearby save room)</li>
<li> Failing a Slot Machine chest and defeating the forced mimic encounter (the mimic encounter is available on its own in a separate chest)</li>
</ul>
<br/>If unset, the above actions will grant you a Star Piece if one is assigned to the associated boss, and unlock the associated map area if the associated boss gates it. Each boss' Star Piece can only be obtained once."""


class NoGenoWhirlExor(BooleanFlag):
    """Setting to disable geno whirl vulnerability on exor"""

    _id: str = "nowhirl"
    _name: str = "No Geno Whirl on Exor"
    _description: str = (
        "If enabled, stunning Exor's eyes will not make him vulnerable to Geno Whirl."
    )


class FixMagikoopa(BooleanFlag):
    """Setting to remove magikoopa big bomb glitch"""

    _id: str = "nobigbang"
    _name: str = "Fix Magikoopa"
    _description: str = (
        "If enabled, King Bomb's Big Bang will not disable Magikoopa's attacks."
    )


class NoOHKO(BooleanFlag):
    """Setting to make boss allies not vulnerable to OHKO"""

    _id: str = "noko"
    _name: str = "No instant KOs on boss allies"
    _description: str = (
        "You will not be able to use Geno Whirl, Pure Water, or Lamb's Lure/Sheep Attack to OHKO any allies to a boss (Mallow Clone, "
        "Bandana Blue, Fautso, etc)."
    )


# ******** Cosmetic


class PaletteSwaps(BooleanFlag):
    """Setting to randomize palettes"""

    _id: str = "palette"
    _name: str = "Palette Swaps"
    _description: str = "Your party members get a change of wardrobe!"


class ChangeNames(BooleanFlag):  # not available unless PaletteSwaps enabled
    """Setting to include name changes with randomized palettes"""

    _id: str = "names"
    _name: str = "Change character names"
    _description: str = (
        """Some palette swaps are references to other media. If this flag is enabled, the character's name will be changed to match the palette."""
    )


class RemakeNames(BooleanFlag):
    """Setting to use the remake's names"""

    _id: str = "renames"
    _name: str = "Use remake names"
    _description: str = (
        """Characters, items, spells, and bosses will use their names from the 2023 Nintendo Switch SMRPG remake. (Palette-driven name changes override this setting for Toadstool.)"""
    )


class JapaneseABXY(BooleanFlag):
    """Setting to use japanese buttons"""

    _id: str = "abxy"
    _name: str = "Japanese ABXY buttons"
    _description: str = (
        "If this flag is enabled, ABXY buttons will have the Super Famicom colours from the Japanese version of the game."
    )


class BossShuffleMusic(BooleanFlag):
    """Setting to randomize boss music"""

    _id: str = "music"
    _name: str = "Randomize boss music"
    _description: str = "Battle music will be randomized for each boss fight."
    inverse__description: str = (
        "(Battle music for each location will remain unchanged from the original game.)"
    )


class ShuffledMusic(CategorizationFlag):
    """Setting to exclude certain music tracks"""

    _id: str = "avail"
    _name: str = "Allowable shuffled music"
    _description: str = """If a song is highlighted (white text over blue), it can appear in any boss fight.
<br>
<br>If a song is not highlighted, it will never appear in a boss fight."""
    _optionEnum = AvailableMusic
    _options: List[AvailableMusic] = BOSS_MUSIC_LIST
    _enabled: List[AvailableMusic] = BOSS_MUSIC_LIST


class RemoveFlashes(BooleanFlag):
    """Setting to remove light flashes"""

    _id: str = "noflash"
    _name: str = "Remove flashes"
    _description: str = """Removes some flashing animations (from spells, attacks, etc).
<br>
<br>Disclaimer: While this feature is intended to promote accessibility, developers cannot promise that every feature in the game with screen flashes has had them removed. Players and viewers with photosensitivity should continue to engage with this randomizer at their own risk. 
<br>
<br>If you would like to suggest an animation that should have flashes removed by this feature, please see the "Contributing" section and fill out the form."""
