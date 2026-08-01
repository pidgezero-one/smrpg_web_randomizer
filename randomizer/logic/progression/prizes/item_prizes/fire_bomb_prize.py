from __future__ import annotations
from randomizer.data.items.items import (FireBombItem)
from randomizer.data.physical_objects.bosses import (SPR0219_RED_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (RedBombObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class FireBombPrize(ItemPrize):
    item = FireBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = RedBombObject
    _packet_data = (SPR0219_RED_ITEM_COLLECTION, 10)


__all__ = ["FireBombPrize"]
