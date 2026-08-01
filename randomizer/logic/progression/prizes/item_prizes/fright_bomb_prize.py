from __future__ import annotations
from randomizer.data.items.items import (FrightBombItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (GreenBombObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class FrightBombPrize(ItemPrize):
    item = FrightBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = GreenBombObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 10)


__all__ = ["FrightBombPrize"]
