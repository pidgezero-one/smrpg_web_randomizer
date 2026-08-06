from __future__ import annotations
from randomizer.data.items.items import (MegaCapeItem)
from randomizer.data.physical_objects.bosses import (SPR0232_CAPE)
from randomizer.data.physical_objects.items import (CapeObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MegaCapePrize(ItemPrize):
    item = MegaCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Cape", description="It looks pretty cool, right?"
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = CapeObject
    _packet_data = (SPR0232_CAPE, 0)


__all__ = ["MegaCapePrize"]
