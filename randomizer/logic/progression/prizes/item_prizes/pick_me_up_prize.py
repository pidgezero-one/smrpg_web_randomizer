from __future__ import annotations
from randomizer.data.items.items import (PickMeUpItem)
from randomizer.data.physical_objects.bosses import (SPR0219_RED_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (StarDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class PickMeUpPrize(ItemPrize):
    item = PickMeUpItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = StarDrinkObject
    _packet_data = (SPR0219_RED_ITEM_COLLECTION, 8)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["PickMeUpPrize"]
