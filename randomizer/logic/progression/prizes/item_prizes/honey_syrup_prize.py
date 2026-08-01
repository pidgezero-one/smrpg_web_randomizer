from __future__ import annotations
from randomizer.data.items.items import (HoneySyrupItem)
from randomizer.data.physical_objects.bosses import (SPR0219_RED_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (RedSyrupObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class HoneySyrupPrize(ItemPrize):
    item = HoneySyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedSyrupObject
    _packet_data = (SPR0219_RED_ITEM_COLLECTION, 1)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["HoneySyrupPrize"]
