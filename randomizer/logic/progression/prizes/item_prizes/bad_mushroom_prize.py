from __future__ import annotations
from randomizer.data.items.items import (BadMushroomItem)
from randomizer.data.physical_objects.bosses import (SPR0223_BLUE_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (BlueMushroomObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class BadMushroomPrize(ItemPrize):
    item = BadMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Mushroom", description="It might be poisonous."
    )
    _model = BlueMushroomObject
    _packet_data = (SPR0223_BLUE_ITEM_COLLECTION, 0)


__all__ = ["BadMushroomPrize"]
