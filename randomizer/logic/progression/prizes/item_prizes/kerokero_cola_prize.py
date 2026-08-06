from __future__ import annotations
from randomizer.data.items.items import (KerokeroColaItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (FrogDrinkObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class KerokeroColaPrize(ItemPrize):
    item = KerokeroColaItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = FrogDrinkObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 6)
    _fortune_type: FortuneEnum = FortuneEnum.DRINK


__all__ = ["KerokeroColaPrize"]
