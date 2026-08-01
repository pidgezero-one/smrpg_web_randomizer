from __future__ import annotations
from randomizer.data.items.items import (BracerItem)
from randomizer.data.physical_objects.bosses import (SPR0221_YELLOW_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (DDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class BracerPrize(ItemPrize):
    item = BracerItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = DDrinkObject
    _packet_data = (SPR0221_YELLOW_ITEM_COLLECTION, 4)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["BracerPrize"]
