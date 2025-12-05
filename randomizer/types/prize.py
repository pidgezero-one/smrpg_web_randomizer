from typing import Optional
from smrpgpatchbuilder.datatypes.items.classes import Item
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import AddToInventory, JmpToEvent, SetBit, RunDialog, PlaySound, DisableObjectTrigger, ActionQueueSync, SetVarToConst
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import A_ObjectMemorySetBit, A_PlaySound, A_VisibilityOff, A_UnknownCommand
from ..data.variables.event_script_names import E3092_STAR_PIECE_GRANT
from ..data.variables.dialog_names import DI3074_GOT_BEETLEMANIA, DI1177_FOUND_A_70A7_AUTO_TERMINATE, DI1178_FOUND_AN_70A7_AUTO_TERMINATE, DI0065_GOT_AN_70A7_AWAIT_TERMINATE, DI0524_GOT_A_70A7_AWAIT_TERMINATE, DI0064_GOT_AN_70A7_AUTO_TERMINATE, DI0066_GOT_A_70A7_AUTO_TERMINATE
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import BOWSER, MARIO, MEM_70A8
from ..data.variables.event_script_names import *
from ..data.variables.variable_names import BEETLEMANIA_UNLOCKED, ITEM_ID, PRIMARY_TEMP_7000
from ..data.variables.overworld_sfx_names import SO027_FOUND_AN_ITEM
from enum import StrEnum

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

    def __init__(self, nickname: str, description: str, starts_with_vowel: Optional[bool] = None):
        self._nickname = nickname
        self._description = description
        if starts_with_vowel is not None:
            self._starts_with_vowel = starts_with_vowel
        else:
            self._starts_with_vowel = nickname[0].lower() in ['a', 'e', 'i', 'o', 'u']
        
    
class Prize:
    _important: bool = False
    _npc_grant: Optional[EventScript] = None
    _chest_grant: Optional[EventScript] = None
    _standing_grant: Optional[EventScript] = None
    _river_grant: Optional[EventScript] = None
    _character_grant: Optional[EventScript] = None
    _spell_grant: Optional[EventScript] = None
    _boss_fight_grant: Optional[EventScript] = None
    _postfight_star_piece_grant: Optional[EventScript] = None
    remake_only: bool = False

    @property
    def important(self) -> bool:
        return self._important
    
    @property
    def npc_grant(self) -> Optional[EventScript]:
        return self._npc_grant
    
    @property
    def chest_grant(self) -> Optional[EventScript]:
        return self._chest_grant
    
    @property
    def standing_grant(self) -> Optional[EventScript]:
        return self._standing_grant

    @property
    def river_grant(self) -> Optional[EventScript]:
        return self._river_grant

    @property
    def character_grant(self) -> Optional[EventScript]:
        return self._character_grant

    @property
    def spell_grant(self) -> Optional[EventScript]:
        return self._spell_grant

    @property
    def boss_fight_grant(self) -> Optional[EventScript]:
        return self._boss_fight_grant

    @property
    def postfight_star_piece_grant(self) -> Optional[EventScript]:
        return self._postfight_star_piece_grant

    def set_important(self, important: bool) -> None:
        self._important = important


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
    _importance: Optional[SpecialItemPrizeType] = None

    @property
    def importance(self) -> Optional[SpecialItemPrizeType]:
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


class StarPiecePrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Shooting Star",
        description="It's sure to make all your wishes\n come true."
    )

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0163_CHEST_GRANT_STAR_PIECE)
        ])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0164_NPC_QUEST_GRANT_STAR_PIECE)
        ])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0166_FREESTANDING_GRANT_STAR_PIECE)
        ])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E2821_ASYNC_NO_ANIMATION_STAR_PIECE)
        ])


class FPFlowerPrize(Prize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, 32),
            JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
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


class ProgressiveItemPrize(StandardPrize):
    pass


class WeddingGearPrize(StandardPrize):
    pass


class EXPStarPrize(Prize):
    _chest_70a7_upper: int = 1

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
        ])


class SlotsPrize(Prize):
    pass


class CharacterPrize(Prize):
    pass


class SpellPrize(Prize):
    pass


class BossFightPrize(Prize):
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

class CoinPrize1(CoinPrize):
    _amount: int = 1
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN)
        ])

    def __init__(self):
        pass

class CoinPrize10(CoinPrize):
    _amount: int = 10
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3146_FREESTANDING_BIG_COIN)
        ])

    def __init__(self):
        pass


class InfiniteCoinPrize(Prize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3074_COIN_CHEST_MULTI_HIT_1)
        ])


class FrogCoinPrize(Prize):
    _amount: int
    _nickname = TreasureHunterNickname(
        nickname="Green Coin",
        description="The exchange rate on this must be\n pretty high."
    )

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(PRIMARY_TEMP_7000, self.amount),
            JmpToEvent(4096) # TODO need a quickhit
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(PRIMARY_TEMP_7000, self.amount),
            JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN)
        ])

    @property
    def amount(self) -> int:
        return self._amount
    
    def __init__(self, amount: int):
        self._amount = amount


class FrogCoinPrize1(FrogCoinPrize):
    _amount: int = 1
    
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([
            SetVarToConst(ITEM_ID, 48),
            JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
        ])
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E0157_NPC_QUEST_GRANT_1_FROG_COIN)
        ])
    @property
    def standing_grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3238_FREESTANDING_FROG_COIN)
        ])

    def __init__(self):
        pass