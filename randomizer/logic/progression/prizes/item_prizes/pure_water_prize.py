from __future__ import annotations
from randomizer.data.items.items import (PureWaterItem)
from randomizer.data.physical_objects.bosses import (SPR0223_BLUE_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (BlueSyrupObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class PureWaterPrize(ItemPrize):
    item = PureWaterItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = BlueSyrupObject
    _packet_data = (SPR0223_BLUE_ITEM_COLLECTION, 1)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["PureWaterPrize"]
