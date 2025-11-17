from smrpgpatchbuilder.datatypes.items.classes import Item
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from ....data.variables.event_script_names import *

class Prize:
    pass


class StandardPrize(Prize):
    _grant: EventScript


class ItemPrize(StandardPrize):
    item: Type[Item]

    @property
    def grant(self) -> EventScript:
        return EventScript([
            AddToInventory(self.item)
        ])


class StarPiecePrize(StandardPrize):
    
    @property
    def grant(self) -> EventScript:
        return EventScript([
            JmpToEvent(E3092_STAR_PIECE_GRANT)
        ])


class BeetlemaniaPrize(StandardPrize):
    pass


class FPFlowerPrize(StandardPrize):
    pass


class FrogCoinPrize(StandardPrize):
    pass


class CoinPrize(StandardPrize):
    pass


class RecoveryMushroomPrize(StandardPrize):
    pass


class WeddingGearPrize(StandardPrize):
    pass


class SlotsPrize(Prize):
    pass


class CharacterPrize(Prize):
    pass


class SpellPrize(Prize):
    pass


class BossFightPrize(Prize):
    pass


class PrizeLocation:
    _prize: Prize
    _missable: bool = False
    _can_accept: list[type[Prize]]

    def set_prize(self, prize: Prize):
        self._prize = prize

    @property
    def prize(self) -> Prize:
        return self._prize

    def __init__(self, prize: Prize):
        self._prize = prize


class TreasureChestLocation(PrizeLocation):
    _can_accept = [
        StandardPrize,
        SlotsPrize,
    ]


class StandingLocation(PrizeLocation):
    _can_accept = [
        StandardPrize,
    ]


class EventLocation(PrizeLocation):
    _can_accept = [
        StandardPrize,
    ]


class BossFightLocation(PrizeLocation):
    _can_accept = [
        BossFightPrize
    ]


class CharacterRecruitmentLocation(PrizeLocation):
    _can_accept = [
        CharacterPrize
    ]


class StarPieceLocation(PrizeLocation):
    _can_accept = [
        StarPiecePrize
    ]


class ShopLocation(PrizeLocation):
    _can_accept = [
        ItemPrize,
    ]


class SpellSlotLocation(PrizeLocation):
    _can_accept = [
        SpellPrize
    ]