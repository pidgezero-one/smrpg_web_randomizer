from __future__ import annotations
from randomizer.data.items.items import (RedEssenceItem)
from randomizer.data.physical_objects.bosses import (SPR0219_RED_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (RedJuiceObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RedEssencePrize(ItemPrize):
    item = RedEssenceItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedJuiceObject
    _packet_data = (SPR0219_RED_ITEM_COLLECTION, 2)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["RedEssencePrize"]
