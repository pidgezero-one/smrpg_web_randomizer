from __future__ import annotations
from randomizer.data.items.items import (SailorCapeItem)
from randomizer.data.physical_objects.bosses import (SPR0232_CAPE)
from randomizer.data.physical_objects.items import (CapeObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SailorCapePrize(ItemPrize):
    item = SailorCapeItem
    _nickname = TreasureHunterNickname(
        nickname="White Cape", description="Built for life on the sea."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = CapeObject
    _packet_data = (SPR0232_CAPE, 0)


__all__ = ["SailorCapePrize"]
