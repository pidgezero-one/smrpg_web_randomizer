from __future__ import annotations
from randomizer.data.items.items import (MidMushroomItem)
from randomizer.data.physical_objects.bosses import (SPR0220_GREEN_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (GreenMushroomObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MidMushroomPrize(ItemPrize):
    item = MidMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Green Mushroom", description="It's just food, right?"
    )
    _model = GreenMushroomObject
    _packet_data = (SPR0220_GREEN_ITEM_COLLECTION, 0)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["MidMushroomPrize"]
