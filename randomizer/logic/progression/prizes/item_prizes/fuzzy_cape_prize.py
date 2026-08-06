from __future__ import annotations
from randomizer.data.items.items import (FuzzyCapeItem)
from randomizer.data.physical_objects.bosses import (SPR0232_CAPE)
from randomizer.data.physical_objects.items import (CapeObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FuzzyCapePrize(ItemPrize):
    item = FuzzyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Cape", description="Made of the finest fleece."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = CapeObject
    _packet_data = (SPR0232_CAPE, 0)


__all__ = ["FuzzyCapePrize"]
