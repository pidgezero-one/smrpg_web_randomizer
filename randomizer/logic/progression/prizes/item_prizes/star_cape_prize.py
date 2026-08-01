from __future__ import annotations
from randomizer.data.items.items import (StarCapeItem)
from randomizer.data.physical_objects.bosses import (SPR0232_CAPE)
from randomizer.data.physical_objects.items import (CapeObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class StarCapePrize(ItemPrize):
    item = StarCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Freedom Cape", description="It's red, white, and blue."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = CapeObject
    _packet_data = (SPR0232_CAPE, 0)


__all__ = ["StarCapePrize"]
