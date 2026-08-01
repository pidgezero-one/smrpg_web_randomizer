from __future__ import annotations
from randomizer.data.items.items import (MegalixirItem)
from randomizer.data.physical_objects.bosses import (SPR0219_RED_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (RedMusicDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MegalixirPrize(ItemPrize):
    item = MegalixirItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedMusicDrinkObject
    _packet_data = (SPR0219_RED_ITEM_COLLECTION, 5)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["MegalixirPrize"]
