from __future__ import annotations
from randomizer.data.items.items import (FryingPanItem)
from randomizer.data.physical_objects.bosses import (SPR0227_FAN_PACKET)
from randomizer.data.physical_objects.items import (FryingPanObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FryingPanPrize(ItemPrize):
    item = FryingPanItem
    _nickname = TreasureHunterNickname(
        nickname="Metal Plate", description="Don't know what it’s used for."
    )
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON
    _model = FryingPanObject
    _packet_data = (SPR0227_FAN_PACKET, 0)


__all__ = ["FryingPanPrize"]
