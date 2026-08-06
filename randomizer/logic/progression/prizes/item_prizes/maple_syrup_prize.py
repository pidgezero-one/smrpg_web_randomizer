from __future__ import annotations
from randomizer.data.items.items import (MapleSyrupItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (GreenSyrupObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MapleSyrupPrize(ItemPrize):
    item = MapleSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = GreenSyrupObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 1)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["MapleSyrupPrize"]
