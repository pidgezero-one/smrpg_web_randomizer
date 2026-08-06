from __future__ import annotations
from randomizer.data.items.items import (AbleJuiceItem)
from randomizer.data.physical_objects.bosses import (SPR0223_BLUE_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (RDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class AbleJuicePrize(ItemPrize):
    item = AbleJuiceItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = RDrinkObject
    _packet_data = (SPR0223_BLUE_ITEM_COLLECTION, 7)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["AbleJuicePrize"]
