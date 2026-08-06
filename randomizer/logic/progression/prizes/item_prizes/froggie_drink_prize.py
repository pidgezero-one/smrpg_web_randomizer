from __future__ import annotations
from randomizer.data.items.items import (FroggieDrinkItem)
from randomizer.data.physical_objects.bosses import (SPR0221_YELLOW_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (YellowMusicDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FroggieDrinkPrize(ItemPrize):
    item = FroggieDrinkItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = YellowMusicDrinkObject
    _packet_data = (SPR0221_YELLOW_ITEM_COLLECTION, 5)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["FroggieDrinkPrize"]
