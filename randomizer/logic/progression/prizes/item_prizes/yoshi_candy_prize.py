from __future__ import annotations
from randomizer.data.items.items import (YoshiCandyItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (GreenCandyObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class YoshiCandyPrize(ItemPrize):
    item = YoshiCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece", description="I wonder what flavor it is?"
    )
    _model = GreenCandyObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 9)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["YoshiCandyPrize"]
