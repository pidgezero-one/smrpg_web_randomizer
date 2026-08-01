from __future__ import annotations
from randomizer.data.items.items import (MaxMushroomItem)
from randomizer.data.physical_objects.bosses import (SPR0221_YELLOW_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (YellowMushroomObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MaxMushroomPrize(ItemPrize):
    item = MaxMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Mushroom", description="It's just food, right?"
    )
    _model = YellowMushroomObject
    _packet_data = (SPR0221_YELLOW_ITEM_COLLECTION, 0)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["MaxMushroomPrize"]
