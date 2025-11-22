from .prize import Prize, StandardPrize, CoinPrize, CoinPrize10, CoinPrize1, EXPStarPrize, SlotsPrize, BossFightPrize, CharacterPrize, StarPiecePrize, ItemPrize, SpellPrize, InfiniteCoinPrize, FPFlowerPrize, ArchipelagoPrize
from ...data.variables.event_script_names import *
from randomizer.types.world.flags import ShuffleLocationSelector
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import DisableObjectTriggerInSpecificLevel
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject


class PrizeLocation:
    _prize: Prize
    _originally_held: type[Prize]
    _missable: bool = False
    _can_accept: list[type[Prize]]
    _rooms: list[int]
    _id: ShuffleLocationSelector
    _remake_only: bool = False

    def set_prize(self, prize: Prize):
        self._prize = prize

    @property
    def prize(self) -> Prize:
        return self._prize
    
    @property
    def originally_held(self) -> type[Prize]:
        return self._originally_held

    def __init__(self, prize: Prize):
        self._prize = prize


class TreasureChestLocation(PrizeLocation):
    _npc_ids: list[AreaObject]
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'chest_grant')
    
    def grant(self) -> EventScript:
        itemgrant = [] if self.prize.chest_grant is None else self.prize.chest_grant.contents
        for npc, room in zip(self._npc_ids, self._rooms):
            itemgrant.append(DisableObjectTriggerInSpecificLevel(AreaObject(npc+14), room))
        return EventScript(itemgrant)


class StandingLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'standing_grant')
    def grant(self) -> EventScript:
        if self.prize.standing_grant is None: return EventScript([])
        return self.prize.standing_grant


class EventLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'npc_grant')
    def grant(self) -> EventScript:
        if self.prize.npc_grant is None: return EventScript([])
        return self.prize.npc_grant

class RiverLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'river_grant')
    def grant(self) -> EventScript:
        if self.prize.river_grant is None: return EventScript([])
        return self.prize.river_grant


class BossFightLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'boss_fight_grant')


class CharacterRecruitmentLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'character_grant')


class StarPieceLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return hasattr(prize, 'postfight_star_piece_grant')


class ShopLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return isinstance(prize, ItemPrize)


class SpellSlotLocation(PrizeLocation):
    def can_accept(self, prize: Prize) -> bool:
        return isinstance(prize, SpellPrize)


class PrizeRow:
    _container_event: int

class TreasureChestLocationRow1(PrizeRow, TreasureChestLocation):
    _container_event: int = E0247_CHEST_1_GRANT

class TreasureChestLocationRow2(PrizeRow, TreasureChestLocation):
    _container_event: int = E0246_CHEST_2_GRANT

class TreasureChestLocationRow3(PrizeRow, TreasureChestLocation):
    _container_event: int = E0245_CHEST_3_GRANT

class TreasureChestLocationRow4(PrizeRow, TreasureChestLocation):
    _container_event: int = E0244_CHEST_4_GRANT

class TreasureChestLocationRow5(PrizeRow, TreasureChestLocation):
    _container_event: int = E0243_CHEST_5_GRANT

class TreasureChestLocationRow6(PrizeRow, TreasureChestLocation):
    _container_event: int = E0242_CHEST_6_GRANT

class NPCLocationRow1(PrizeRow, EventLocation):
    _container_event: int = E0253_NPC_QUEST_1_GRANT

class NPCLocationRow2(PrizeRow, EventLocation):
    _container_event: int = E0252_NPC_QUEST_2_GRANT

class NPCLocationRow3(PrizeRow, EventLocation):
    _container_event: int = E0251_NPC_QUEST_3_GRANT

class NPCLocationRow4(PrizeRow, EventLocation):
    _container_event: int = E0250_NPC_QUEST_4_GRANT

class NPCLocationRow5(PrizeRow, EventLocation):
    _container_event: int = E0249_NPC_QUEST_5_GRANT

class NPCLocationRow6(PrizeRow, EventLocation):
    _container_event: int = E0248_NPC_QUEST_6_GRANT

class NPCLocationRow7(PrizeRow, EventLocation):
    _container_event: int = E0226_NPC_QUEST_7_GRANT

class StandingLocationRow1(PrizeRow, StandingLocation):
    _container_event: int = E0241_FREESTANDING_1_GRANT

class StandingLocationRow2(PrizeRow, StandingLocation):
    _container_event: int = E0240_FREESTANDING_2_GRANT

class StandingLocationRow3(PrizeRow, StandingLocation):
    _container_event: int = E0239_FREESTANDING_3_GRANT

class StandingLocationRow4(PrizeRow, StandingLocation):
    _container_event: int = E0238_FREESTANDING_4_GRANT

class StandingLocationRow5(PrizeRow, StandingLocation):
    _container_event: int = E0237_FREESTANDING_5_GRANT

class StandingLocationRow6(PrizeRow, StandingLocation):
    _container_event: int = E0236_FREESTANDING_6_GRANT

class StandingLocationRow7(PrizeRow, StandingLocation):
    _container_event: int = E0235_FREESTANDING_7_GRANT

class StandingLocationRow8(PrizeRow, StandingLocation):
    _container_event: int = E0234_FREESTANDING_8_GRANT

class StandingLocationRow9(PrizeRow, StandingLocation):
    _container_event: int = E0233_FREESTANDING_9_GRANT

class StandingLocationRow10(PrizeRow, StandingLocation):
    _container_event: int = E0232_FREESTANDING_10_GRANT

class StandingLocationRow11(PrizeRow, StandingLocation):
    _container_event: int = E0231_FREESTANDING_11_GRANT

class StandingLocationRow12(PrizeRow, StandingLocation):
    _container_event: int = E0230_FREESTANDING_12_GRANT

class StandingLocationRow13(PrizeRow, StandingLocation):
    _container_event: int = E0229_FREESTANDING_13_GRANT

class StandingLocationRow14(PrizeRow, StandingLocation):
    _container_event: int = E0228_FREESTANDING_14_GRANT

class StandingLocationRow15(PrizeRow, StandingLocation):
    _container_event: int = E0227_FREESTANDING_15_GRANT

class RiverLocationRow1(PrizeRow, RiverLocation):
    _container_event: int = E0253_NPC_QUEST_1_GRANT

class RiverLocationRow2(PrizeRow, RiverLocation):
    _container_event: int = E0241_FREESTANDING_1_GRANT