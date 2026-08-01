from __future__ import annotations
from randomizer.data.items.items import (HappyCapeItem)
from randomizer.data.physical_objects.bosses import (SPR0232_CAPE)
from randomizer.data.physical_objects.items import (CapeObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class HappyCapePrize(ItemPrize):
    item = HappyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Cape", description="I'd be proud to wear this!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = CapeObject
    _packet_data = (SPR0232_CAPE, 0)


__all__ = ["HappyCapePrize"]
