from __future__ import annotations
import random
from typing import TYPE_CHECKING, TypeVar
from .physical_objects import BossNPC, ItemNPC, HenchmanNPC
from ..data.physical_objects.items import DefaultItem

from smrpgpatchbuilder.datatypes.items.classes import Item
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpToEvent,
    SetVarToConst,
    PlaySound,
    Inc,
    Return,
    SetBit,
)
from ..data.variables.event_script_names import E3092_STAR_PIECE_GRANT
from ..data.variables.event_script_names import *
from ..data.variables.variable_names import (
    ITEM_ID,
    PRIMARY_TEMP_7000,
    TEMP_7032,
)
from enum import StrEnum
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
)
from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell
from ..types.ally import Ally
from ..data.variables.overworld_sfx_names import SO081_STAR
from ..data.physical_objects.items import *
from ..types.enemy import Enemy
from ..data.variables.overworld_sfx_names import *

if TYPE_CHECKING:
    from .gameworld import GameWorld
    from .prizelocation import PrizeLocation


class TreasureHunterNickname:
    _nickname: str
    _starts_with_vowel: bool
    _description: str

    @property
    def description(self) -> str:
        return self._description

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def starts_with_vowel(self) -> bool:
        return self._starts_with_vowel

    @property
    def article(self) -> str:
        return "An" if self._starts_with_vowel else "A"

    def get_slot_1_dialog(self) -> str:
        return f" Item #1: {self.article} “{self._nickname}”!\n {self._description}[await][page]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]"

    def get_slot_2_dialog(self) -> str:
        return f" Item #2: {self.article} “{self._nickname}”.\n {self._description}[await][page]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]"

    def get_slot_3_dialog(self) -> str:
        return f" Item #3: {self.article} “{self._nickname}”.\n {self._description}[await][page]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]"

    def __init__(
        self, nickname: str, description: str, starts_with_vowel: bool | None = None
    ):
        self._nickname = nickname
        self._description = description
        if starts_with_vowel is not None:
            self._starts_with_vowel = starts_with_vowel
        else:
            self._starts_with_vowel = nickname[0].lower() in ["a", "e", "i", "o", "u"]


class Prize:
    _important: bool = False
    _npc_grant: EventScript | None = None
    _chest_grant: EventScript | None = None
    _standing_grant: EventScript | None = None
    _river_grant: EventScript | None = None
    _hill_grant: EventScript | None = None
    _character_grant: EventScript | None = None
    _spell_grant: EventScript | None = None
    _boss_fight_grant: EventScript | None = None
    _postfight_star_piece_grant: EventScript | None = None
    remake_only: bool = False
    key: bool = False
    _model: type[ItemNPC] | None = DefaultItem
    _sound_effect: int = SO014_FLOWER

    @property
    def sound_effect(self) -> int:
        return self._sound_effect
    
    @property
    def model(self) -> type[ItemNPC] | None:
        return self._model

    @property
    def important(self) -> bool:
        return self._important

    @property
    def npc_grant(self) -> EventScript | None:
        return self._npc_grant

    @property
    def chest_grant(self) -> EventScript | None:
        return self._chest_grant

    @property
    def standing_grant(self) -> EventScript | None:
        return self._standing_grant

    @property
    def river_grant(self) -> EventScript | None:
        return self._river_grant

    @property
    def hill_grant(self) -> EventScript | None:
        return self._hill_grant

    @property
    def character_grant(self) -> EventScript | None:
        return self._character_grant

    @property
    def spell_grant(self) -> EventScript | None:
        return self._spell_grant

    @property
    def boss_fight_grant(self) -> EventScript | None:
        return self._boss_fight_grant

    @property
    def postfight_star_piece_grant(self) -> EventScript | None:
        return self._postfight_star_piece_grant

    def set_important(self, important: bool) -> None:
        self._important = important


TOriginallyHeld = TypeVar("TOriginallyHeld", bound=type[Prize] | None)

class KeyPrize(Prize):
    pass


class StandardPrize(Prize):
    _grant: EventScript
    _nickname: TreasureHunterNickname

    @property
    def nickname(self) -> TreasureHunterNickname:
        return self._nickname


class SpecialItemPrizeType(StrEnum):
    KEY = "key"
    SPECIAL_EQUIP_TIER_1 = "special_equip_tier_1"
    SPECIAL_EQUIP_TIER_2 = "special_equip_tier_2"


class ItemPrize(StandardPrize):
    item: type[Item]
    _importance: SpecialItemPrizeType | None = None
    _monstro_shuffle: bool = False

    @property
    def importance(self) -> SpecialItemPrizeType | None:
        return self._importance

    @property
    def chest_grant(self) -> EventScript:
        if self.model is not None:
            return EventScript(
                [
                    SetVarToConst(ITEM_ID, self.item().item_id),
                    JmpToEvent(self.model._chest_event_id),
                ]
            )
        return EventScript(
            [
                SetVarToConst(ITEM_ID, self.item().item_id),
                JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, self.item().item_id),
                JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
            ]
        )

    @property
    def standing_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, self.item().item_id),
                JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG),
            ]
        )

    @property
    def river_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, self.item().item_id),
                JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
            ]
        )

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [SetVarToConst(ITEM_ID, self.item().item_id), JmpToEvent(E0215_HILL_ITEM)]
        )


class StarPiecePrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Shooting Star",
        description="It's sure to make all your wishes\n come true.",
    )
    _hint: Flag
    _model = TinyStarObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [SetBit(self._hint), JmpToEvent(E0163_CHEST_GRANT_STAR_PIECE)]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript(
            [SetBit(self._hint), JmpToEvent(E0164_NPC_QUEST_GRANT_STAR_PIECE)]
        )

    @property
    def standing_grant(self) -> EventScript:
        return EventScript(
            [SetBit(self._hint), JmpToEvent(E0166_FREESTANDING_GRANT_STAR_PIECE)]
        )

    @property
    def river_grant(self) -> EventScript:
        return EventScript(
            [SetBit(self._hint), JmpToEvent(E2821_ASYNC_NO_ANIMATION_STAR_PIECE)]
        )

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(TEMP_7032),
                SetBit(self._hint),
                PlaySound(sound=SO081_STAR, channel=4),
                Return(),
            ]
        )

    @property
    def postfight_star_piece_grant(self) -> EventScript:
        return EventScript([SetBit(self._hint), JmpToEvent(E3092_STAR_PIECE_GRANT)])


class FPFlowerPrize(Prize):
    _model = FlowerObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 32),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0216_GET_FLOWER_FROM_NPC)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E1801_FREESTANDING_FLOWER)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2817_ASYNC_NO_ANIMATION_FLOWER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0214_HILL_GET_FLOWER)])


class ProgressiveItemPrize(StandardPrize):
    pass


class WeddingGearPrize(StandardPrize):
    pass


class EXPStarPrize(Prize):
    pass


class SlotsPrize(Prize):
    _logic_event: int

    @property
    def logic_event(self) -> int:
        return self._logic_event

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(self.logic_event)])



class CharacterName:
    placeholder: str = "`NAME`"
    gender: str = "man"
    gender_casual: str = "guy"
    honorific: str = "sir"
    title: str = "mister"
    title_short: str = "Mr"
    mole_greeting: str = "mate"
    mboy_greeting: str = ", man"

    def __init__(
        self,
        placeholder: str = "`NAME`",
        gender: str = "man",
        gender_casual: str = "guy",
        honorific: str = "sir",
        title: str = "mister",
        title_short: str = "Mr",
        mole_greeting: str = "mate",
        mboy_greeting: str = ", man",
    ) -> None:
        self.placeholder = placeholder
        self.gender = gender
        self.gender_casual = gender_casual
        self.honorific = honorific
        self.title = title
        self.title_short = title_short
        self.mole_greeting = mole_greeting
        self.mboy_greeting = mboy_greeting


class CharacterPrize(Prize):
    _ally: Ally
    _starting_level: int = 1
    _name_props: CharacterName
    _character_model: NPC

    @property
    def character_model(self) -> NPC:
        return self._character_model

    @property
    def ally(self) -> Ally:
        return self._ally

    @property
    def name_props(self) -> CharacterName:
        return self._name_props

    @property
    def starting_level(self) -> int:
        return self._starting_level

    def set_starting_level(self, level: int) -> None:
        self._starting_level = level

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        return EventScript([Return()])

    @property
    def character_grant(self) -> EventScript:
        return EventScript([])


class SpellPrize(Prize):
    _spell: type[CharacterSpell]

    @property
    def spell(self) -> type[CharacterSpell]:
        return self._spell


class BossFightHenchman:
    _monster: type[Enemy]
    _model: type[HenchmanNPC]

    @property
    def monster(self) -> type[Enemy]:
        return self._monster

    @property
    def model(self) -> type[HenchmanNPC]:
        return self._model

    def __init__(
        self,
        monster: type[Enemy],
        model: type[HenchmanNPC],
    ):
        self._monster = monster
        self._model = model


class BossFightPrize(Prize):
    _members: list[FormationMember]
    _force_battlefield: Battlefield | None = None
    _force_start_event: int | None = None
    _text: str

    _big_npc: type[BossNPC] | None = None
    _battle_npc: type[BossNPC] | None = None
    _small_npc: type[BossNPC] 
    _statue_npc: type[BossNPC] | None = None

    _character_henchmen: list[BossFightHenchman] | None = None
    _mook_henchmen: list[BossFightHenchman] | None = None
    _tiny_henchmen: list[BossFightHenchman] | None = None

    # Stat scaling configuration
    # Enemies whose HP can be scaled proportionally but should NOT receive a slice of the HP "pie"
    # (e.g., Culex's crystals, Johnny's bandana blues - the main boss gets all the HP)
    _hp_slice_excluded_enemies: list[type[Enemy]] = []
    # Additional enemies outside the formation that should also receive stat scaling
    _additional_enemies_to_scale: list[type[Enemy]] = []
    # The anchor enemy(s) for stat ratio calculations - other enemies' stats scale relative to this
    # If None, uses the average of all formation members as the reference
    # If a single enemy class, uses that enemy's stats as reference
    # If a list of enemy classes, uses the average of those specific enemies as reference
    _anchor_enemy: type[Enemy] | list[type[Enemy]] | None = None
    # Extra enemies to include in HP slicing beyond what's in the formation
    # (e.g., King Calamari has more tentacles in battle than formation can hold)
    # Each entry represents one enemy instance
    _extra_hp_enemies: list[type[Enemy]] = []
    # Enemies to completely exclude from scaling for this prize
    # (e.g., WaterCrystal in Johnny's formation is only there for graphical fix, not actual combat)
    # These enemies won't be scaled and won't count toward HP slicing or reference calculations
    _scaling_excluded_enemies: list[type[Enemy]] = []
    # Multiplier applied to the location's HP total when this prize is the original
    # (e.g., Cloaker/Domino fight has 4 enemies but you only fight 2, so multiply by 0.5)
    _location_hp_multiplier: float = 1.0
    # Multipliers for how much an enemy counts toward the pie total when dividing HP
    # (e.g., Dodo in Valentina fight counts as 40% of his HP when dividing the pie)
    _hp_pie_contribution_multipliers: dict[type[Enemy], float] = {}
    # Multipliers applied to an enemy's HP slice after calculation
    # (e.g., Dodo in Valentina fight gets 2.5x his calculated HP slice)
    _hp_slice_multipliers: dict[type[Enemy], float] = {}

    _name: str = ""
    _remake_name: str = ""
    _canon_name: str = ""
    _seaside_letter_name_if_sunken_ship_boss: str = ""
    _seaside_letter_name_if_sunken_ship_boss_remake: str = ""
    _seaside_letter_name_if_sunken_ship_boss_canon: str = ""
    _seaside_letter_name_if_volcano_boss: str = ""
    _seaside_letter_name_if_volcano_boss_remake: str = ""
    _seaside_letter_name_if_volcano_boss_canon: str = ""
    _seaside_letter_name_if_final_boss: str = ""
    _seaside_letter_name_if_final_boss_remake: str = ""
    _seaside_letter_name_if_final_boss_canon: str = ""
    _seaside_letter_name_if_seaside_boss: str = ""
    _seaside_letter_name_if_seaside_boss_remake: str = ""
    _seaside_letter_name_if_seaside_boss_canon: str = ""

    _dialog_replacements: dict[int, str] | None = None
    _dialog_replacements_remake: dict[int, str] | None = None
    _dialog_replacements_canon: dict[int, str] | None = None
    _dialog_replacements_if_mandatory_fights_changed: dict[int, str] | None = None
    _dialog_replacements_if_mandatory_fights_changed_remake: dict[int, str] | None = (
        None
    )
    _dialog_replacements_if_mandatory_fights_changed_canon: dict[int, str] | None = None
    _dialog_replacements_peach: dict[int, str] | None = None
    _dialog_replacements_if_mandatory_fights_changed_peach: dict[int, str] | None = None
    _dialog_replacements_canon_and_remake: dict[int, str] | None = None

    @property
    def character_henchmen(self) -> list[BossFightHenchman] | None:
        return self._character_henchmen

    @property
    def mook_henchmen(self) -> list[BossFightHenchman] | None:
        return self._mook_henchmen

    @property
    def tiny_henchmen(self) -> list[BossFightHenchman] | None:
        return self._tiny_henchmen

    @property
    def hp_slice_excluded_enemies(self) -> list[type[Enemy]]:
        """Enemies whose HP can be scaled proportionally but should NOT receive a slice of the HP pie."""
        return self._hp_slice_excluded_enemies

    @property
    def additional_enemies_to_scale(self) -> list[type[Enemy]]:
        """Additional enemies outside the formation that should also receive stat scaling."""
        return self._additional_enemies_to_scale

    @property
    def anchor_enemy(self) -> type[Enemy] | list[type[Enemy]] | None:
        """The anchor enemy(s) for stat ratio calculations. Other enemies' stats scale relative to this."""
        return self._anchor_enemy

    @property
    def extra_hp_enemies(self) -> list[type[Enemy]]:
        """Extra enemies to include in HP slicing beyond what's in the formation."""
        return self._extra_hp_enemies

    @property
    def scaling_excluded_enemies(self) -> list[type[Enemy]]:
        """Enemies to completely exclude from scaling for this prize."""
        return self._scaling_excluded_enemies

    @property
    def location_hp_multiplier(self) -> float:
        """Multiplier applied to the location's HP total when this prize is the original."""
        return self._location_hp_multiplier

    @property
    def hp_pie_contribution_multipliers(self) -> dict[type[Enemy], float]:
        """Multipliers for how much an enemy counts toward the pie total when dividing HP."""
        return self._hp_pie_contribution_multipliers

    @property
    def hp_slice_multipliers(self) -> dict[type[Enemy], float]:
        """Multipliers applied to an enemy's HP slice after calculation."""
        return self._hp_slice_multipliers

    @property
    def battle_npc(self) -> type[BossNPC]:
        if self._battle_npc is not None:
            return self._battle_npc
        if self._big_npc is not None:
            return self._big_npc
        return self._small_npc

    @property
    def large_npc(self) -> type[BossNPC]:
        if self._big_npc is not None:
            return self._big_npc
        return self._small_npc

    @property
    def small_npc(self) -> type[BossNPC]:
        return self._small_npc

    @property
    def statue_npc(self) -> type[BossNPC] | None:
        return self._statue_npc

    def get_dialog_replacements(
        self,
        remake: bool = False,
        canon: bool = False,
        mandatory_fights_changed: bool = False,
        peach: bool = False,
    ) -> dict[int, str]:
        if not self._dialog_replacements:
            return {}
        dialog_replacements = {**self._dialog_replacements}
        if remake:
            dialog_replacements = {
                **dialog_replacements,
                **(self._dialog_replacements_remake or {}),
            }
        if canon:
            dialog_replacements = {
                **dialog_replacements,
                **(self._dialog_replacements_canon or {}),
            }
        if canon and remake:
            dialog_replacements = {
                **dialog_replacements,
                **(self._dialog_replacements_canon_and_remake or {}),
            }
        if peach:
            dialog_replacements = {
                **dialog_replacements,
                **(self._dialog_replacements_peach or {}),
            }
        if mandatory_fights_changed:
            dialog_replacements = {
                **dialog_replacements,
                **(self._dialog_replacements_if_mandatory_fights_changed or {}),
            }
            if remake:
                dialog_replacements = {
                    **dialog_replacements,
                    **(
                        self._dialog_replacements_if_mandatory_fights_changed_remake
                        or {}
                    ),
                }
            if canon:
                dialog_replacements = {
                    **dialog_replacements,
                    **(
                        self._dialog_replacements_if_mandatory_fights_changed_canon
                        or {}
                    ),
                }
            if peach:
                dialog_replacements = {
                    **dialog_replacements,
                    **(
                        self._dialog_replacements_if_mandatory_fights_changed_peach
                        or {}
                    ),
                }
        return dialog_replacements

    def seaside_letter_name_if_sunken_ship_boss(
        self, remake: bool = False, canon: bool = False
    ) -> str:
        if canon:
            return (
                self._seaside_letter_name_if_sunken_ship_boss_canon
                or self._seaside_letter_name_if_sunken_ship_boss_remake
                or self._seaside_letter_name_if_sunken_ship_boss
                or self._canon_name
                or self._remake_name
                or self._name
                or self._text
            )
        if remake:
            return (
                self._seaside_letter_name_if_sunken_ship_boss_remake
                or self._seaside_letter_name_if_sunken_ship_boss
                or self._remake_name
                or self._name
                or self._text
            )
        return self._seaside_letter_name_if_sunken_ship_boss or self._name or self._text

    def seaside_letter_name_if_volcano_boss(
        self, remake: bool = False, canon: bool = False
    ) -> str:
        if canon:
            return (
                self._seaside_letter_name_if_volcano_boss_canon
                or self._seaside_letter_name_if_volcano_boss_remake
                or self._seaside_letter_name_if_volcano_boss
            )
        if remake:
            return (
                self._seaside_letter_name_if_volcano_boss_remake
                or self._seaside_letter_name_if_volcano_boss
            )
        return self._seaside_letter_name_if_volcano_boss

    def seaside_letter_name_if_final_boss(
        self, remake: bool = False, canon: bool = False
    ) -> str:
        if canon:
            return (
                self._seaside_letter_name_if_final_boss_canon
                or self._seaside_letter_name_if_final_boss_remake
                or self._seaside_letter_name_if_final_boss
            )
        if remake:
            return (
                self._seaside_letter_name_if_final_boss_remake
                or self._seaside_letter_name_if_final_boss
            )
        return self._seaside_letter_name_if_final_boss

    def seaside_letter_name_if_seaside_boss(
        self, remake: bool = False, canon: bool = False
    ) -> str:
        if canon:
            return (
                self._seaside_letter_name_if_seaside_boss_canon
                or self._seaside_letter_name_if_seaside_boss_remake
                or self._seaside_letter_name_if_seaside_boss
                or self._canon_name
                or self._remake_name
                or self._name
                or self._text
            )
        if remake:
            return (
                self._seaside_letter_name_if_seaside_boss_remake
                or self._seaside_letter_name_if_seaside_boss
                or self._remake_name
                or self._name
                or self._text
            )
        return self._seaside_letter_name_if_seaside_boss or self._name or self._text

    def name(self, remake: bool = False, canon: bool = False) -> str:
        if canon:
            return self._canon_name or self._remake_name or self._name or self._text
        if remake:
            return self._remake_name or self._name or self._text
        return self._name or self._text

    @property
    def formation(self) -> list[FormationMember]:
        return self._members

    @property
    def force_battlefield(self) -> Battlefield | None:
        return self._force_battlefield

    @property
    def force_start_event(self) -> int | None:
        return self._force_start_event

    @property
    def boss_fight_grant(self) -> EventScript | None:
        return EventScript([Return()])

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        return EventScript([Return()])

    def unlocks(self, world: GameWorld) -> EventScript:
        return EventScript([Return()])


class MimicFightInitiatorPrize(Prize):
    pass


class EmptyPrize(Prize):

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3081_YOU_MISSED)])


class ArchipelagoPrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Mysterious Item", description="A friend of yours is looking for it."
    )


class CoinPrize(Prize):
    _model = BigCoinObject
    _amount: int
    _nickname = TreasureHunterNickname(
        nickname="Gold Coin",
        description=" They're nothing special, but a guy's\n gotta eat.",
    )

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(PRIMARY_TEMP_7000, self.amount),
                JmpToEvent(E3080_COIN_CHEST_QUICK_HIT), 
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(PRIMARY_TEMP_7000, self.amount),
                JmpToEvent(E0159_NPC_QUEST_GRANT_COINS),
            ]
        )

    @property
    def amount(self) -> int:
        return self._amount

    def __init__(self, amount: int):
        self._amount = amount


class FrogCoinPrize(StandardPrize):
    _model = FrogCoinObject
    _amount: int
    _nickname = TreasureHunterNickname(
        nickname="Green Coin",
        description="The exchange rate on this must be\n pretty high.",
    )

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(PRIMARY_TEMP_7000, self.amount),
                JmpToEvent(E3084_FROG_COIN_CHEST_QUICK_HIT), 
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        if self.amount == 1:
            return EventScript([JmpToEvent(E0157_NPC_QUEST_GRANT_1_FROG_COIN)])
        return EventScript(
            [
                SetVarToConst(PRIMARY_TEMP_7000, self.amount),
                JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
            ]
        )

    @property
    def amount(self) -> int:
        return self._amount

    def __init__(self, amount: int):
        self._amount = amount


class FrogCoinQuantityPrize(FrogCoinPrize):
    def __init__(self):
        super().__init__(self._amount)


class CoinQuantityPrize(CoinPrize):
    def __init__(self):
        super().__init__(self._amount)


# This gets placed in a location where item quality != original_pool
# and will be used to generate an item on the fly
class RandomPrizeSubstitute(Prize):
    def generate(self, world: GameWorld, location: PrizeLocation) -> Prize:
        # Lazy imports to avoid circular imports
        from .flags import ItemQuality, ItemQualityOptions, BiasItemShuffle
        from ..progression.prizes import (
            RecoveryMushroomPrize,
            FrogCoin1Prize,
            Coins10Prize,
        )

        pool: list[type] = []
        if world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.COMPLETELY_RANDOM
        ):
            if world.settings.isflag_enabled(BiasItemShuffle):
                if location._bias:
                    pool = (
                        world.high_impact_items
                        + world.highest_impact_items
                        + world.high_impact_equip
                        + world.highest_impact_equip
                    )
                else:
                    pool = (
                        world.low_impact_items
                        + world.high_impact_items
                        + world.low_impact_equip
                        + world.high_impact_equip
                    )
            else:
                pool = (
                    world.low_impact_items
                    + world.high_impact_items
                    + world.highest_impact_items
                    + world.low_impact_equip
                    + world.high_impact_equip
                    + world.highest_impact_equip
                )
            chosen_item = random.choice(pool)
            return world.item_to_prize.get(chosen_item)()  # type: ignore
        elif world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.MOSTLY_RANDOM
        ):
            roll = random.randint(1, 100)
            if world.settings.isflag_enabled(BiasItemShuffle):
                if location._bias:
                    if roll <= 40:
                        pool = world.high_impact_items + world.high_impact_equip
                    elif roll <= 95:
                        pool = world.low_impact_items + world.low_impact_equip
                    else:
                        pool = world.highest_impact_items + world.highest_impact_equip
                else:
                    if roll <= 75:
                        pool = world.low_impact_items + world.low_impact_equip
                    elif roll <= 99:
                        pool = world.high_impact_items + world.high_impact_equip
                    else:
                        pool = world.highest_impact_items + world.highest_impact_equip
            else:
                if roll <= 65:
                    pool = world.low_impact_items + world.low_impact_equip
                elif roll <= 95:
                    pool = world.high_impact_items + world.high_impact_equip
                else:
                    pool = world.highest_impact_items + world.highest_impact_equip
            chosen_item = random.choice(pool)
            return world.item_to_prize.get(chosen_item)()  # type: ignore
        elif world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY
        ):
            return EmptyPrize()
        else:
            return random.choice(
                [
                    FPFlowerPrize,
                    RecoveryMushroomPrize,
                    FrogCoin1Prize,
                    Coins10Prize,
                ]
            )()
