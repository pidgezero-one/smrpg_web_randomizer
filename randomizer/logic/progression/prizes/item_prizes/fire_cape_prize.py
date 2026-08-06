from __future__ import annotations
from randomizer.data.items.items import (FireCapeItem)
from randomizer.data.physical_objects.bosses import (SPR0232_CAPE)
from randomizer.data.physical_objects.items import (CapeObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FireCapePrize(ItemPrize):
    item = FireCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Cape", description="The pattern on it is pretty cool."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = CapeObject
    _packet_data = (SPR0232_CAPE, 0)


__all__ = ["FireCapePrize"]
