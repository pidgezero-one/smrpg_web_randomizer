from __future__ import annotations
from randomizer.data.items.items import (IceBombItem)
from randomizer.data.physical_objects.bosses import (SPR0223_BLUE_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (BlueBombObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class IceBombPrize(ItemPrize):
    item = IceBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = BlueBombObject
    _packet_data = (SPR0223_BLUE_ITEM_COLLECTION, 10)


__all__ = ["IceBombPrize"]
