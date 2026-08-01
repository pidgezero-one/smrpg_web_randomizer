from __future__ import annotations
from randomizer.data.items.items import (RockCandyItem)
from randomizer.data.physical_objects.bosses import (SPR0223_BLUE_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (BlueCandyObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class RockCandyPrize(ItemPrize):
    item = RockCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece", description="I wonder what flavor it is?"
    )
    _model = BlueCandyObject
    _packet_data = (SPR0223_BLUE_ITEM_COLLECTION, 9)


__all__ = ["RockCandyPrize"]
