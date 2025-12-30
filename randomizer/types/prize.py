from __future__ import annotations
import random
from typing import TYPE_CHECKING
from .physical_objects import ItemNPC
from ..data.physical_objects.items import DefaultItem

from smrpgpatchbuilder.datatypes.items.classes import Item
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import JmpToEvent, SetVarToConst, PlaySound, Inc, Return, SetBit
from ..data.variables.event_script_names import E3092_STAR_PIECE_GRANT
from ..data.variables.dialog_names import DI3074_GOT_BEETLEMANIA, DI1177_FOUND_A_70A7_AUTO_TERMINATE, DI1178_FOUND_AN_70A7_AUTO_TERMINATE, DI0065_GOT_AN_70A7_AWAIT_TERMINATE, DI0524_GOT_A_70A7_AWAIT_TERMINATE, DI0064_GOT_AN_70A7_AUTO_TERMINATE, DI0066_GOT_A_70A7_AUTO_TERMINATE
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import BOWSER, MARIO, MEM_70A8
from ..data.variables.event_script_names import *
from ..data.variables.variable_names import BEETLEMANIA_UNLOCKED, ITEM_ID, PRIMARY_TEMP_7000, TEMP_7032
from ..data.variables.overworld_sfx_names import SO027_FOUND_AN_ITEM
from enum import StrEnum
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import Formation, FormationMember
from smrpgpatchbuilder.datatypes.characters.classes import Character
from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell
from ..types.ally import Ally
from ..data.variables.overworld_sfx_names import SO081_STAR
from ..data.physical_objects.items import *

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

    def __init__(self, nickname: str, description: str, starts_with_vowel: bool | None = None):
        self._nickname = nickname
        self._description = description
        if starts_with_vowel is not None:
            self._starts_with_vowel = starts_with_vowel
        else:
            self._starts_with_vowel = nickname[0].lower() in ['a', 'e', 'i', 'o', 'u']
        
# TODO: packets/models    
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
        return EventScript([
            SetVarToConst(ITEM_ID, self.item().item_id),
            JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST)
        ])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, self.item().item_id),
            JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
        ])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, self.item().item_id),
            JmpToEvent(E0165_FREESTANDING_GRANT_ITEM_BAG)
        ])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, self.item().item_id),
            JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM)
        ])
    
    @property
    def hill_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, self.item().item_id),
            JmpToEvent(E0215_HILL_ITEM)
        ])


class StarPiecePrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Shooting Star",
        description="It's sure to make all your wishes\n come true."
    )
    _hint: Flag
    _model = TinyStarObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetBit(self._hint),
            JmpToEvent(E0163_CHEST_GRANT_STAR_PIECE)
        ])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            SetBit(self._hint),
            JmpToEvent(E0164_NPC_QUEST_GRANT_STAR_PIECE)
        ])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            SetBit(self._hint),
            JmpToEvent(E0166_FREESTANDING_GRANT_STAR_PIECE)
        ])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            SetBit(self._hint),
            JmpToEvent(E2821_ASYNC_NO_ANIMATION_STAR_PIECE)
        ])
    
    @property
    def hill_grant(self) -> EventScript:
        return EventScript([
            Inc(TEMP_7032),
            SetBit(self._hint),
            PlaySound(sound=SO081_STAR, channel=4),
            Return(),
        ])
    
    @property
    def postfight_star_piece_grant(self) -> EventScript:
        return EventScript([
            SetBit(self._hint),
            JmpToEvent(E3092_STAR_PIECE_GRANT)
        ])


class FPFlowerPrize(Prize):
    _model = FlowerObject
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, 32),
            JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0216_GET_FLOWER_FROM_NPC)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E1801_FREESTANDING_FLOWER)
        ])
    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E2817_ASYNC_NO_ANIMATION_FLOWER)
        ])
    @property
    def hill_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0214_HILL_GET_FLOWER)
        ])


class ProgressiveItemPrize(StandardPrize):
    pass


class WeddingGearPrize(StandardPrize):
    pass


class EXPStarPrize(Prize):
    pass

class SlotsPrize(Prize):
    # TODO
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            Return()
        ])
    pass


class CharacterPrize(Prize):
    _ally: Ally
    _starting_level: int = 1

    @property
    def ally(self) -> Ally:
        return self._ally
    
    @property
    def starting_level(self) -> int:
        return self._starting_level
    
    def set_starting_level(self, level: int) -> None:
        self._starting_level = level

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        return EventScript([
            Return()
        ])

    @property
    def character_grant(self) -> EventScript:
        return EventScript([])


class SpellPrize(Prize):
    _spell: type[CharacterSpell]

    @property
    def spell(self) -> type[CharacterSpell]:
        return self._spell


class BossFightPrize(Prize):
    _members: list[FormationMember]
    _force_battlefield: Battlefield | None
    _force_start_event: int | None
    _text: str

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
        return EventScript([
            Return()
        ])
    
    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        return EventScript([
            Return()
        ])

    def unlocks(self, world: GameWorld) -> EventScript:
        return EventScript([
            Return()
        ])

class MimicFightInitiatorPrize(Prize):
    pass

class EmptyPrize(Prize):

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3081_YOU_MISSED)
        ])



class ArchipelagoPrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Mysterious Item",
        description="A friend of yours is looking for it."
    )


class CoinPrize(Prize):
    _model = BigCoinObject
    _amount: int
    _nickname = TreasureHunterNickname(
        nickname="Gold Coin",
        description=" They're nothing special, but a guy's\n gotta eat."
    )
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(PRIMARY_TEMP_7000, self.amount),
            JmpToEvent(E3080_COIN_CHEST_QUICK_HIT) # TODO: this is wrong
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(PRIMARY_TEMP_7000, self.amount),
            JmpToEvent(E0159_NPC_QUEST_GRANT_COINS)
        ])

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
        description="The exchange rate on this must be\n pretty high."
    )

    @property
    def chest_grant(self) -> EventScript:
        if self.amount == 1:
            return EventScript([
            SetVarToConst(ITEM_ID, 48),
            JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
            ])
        return EventScript([
            SetVarToConst(PRIMARY_TEMP_7000, self.amount),
            JmpToEvent(E3082_FROG_COIN_CHEST_MULTI_HIT_1)
        ])
    @property
    def npc_grant(self) -> EventScript:
        if self.amount == 1:
            return EventScript([
                JmpToEvent(E0157_NPC_QUEST_GRANT_1_FROG_COIN)
            ])
        return EventScript([
            SetVarToConst(PRIMARY_TEMP_7000, self.amount),
            JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN)
        ])

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