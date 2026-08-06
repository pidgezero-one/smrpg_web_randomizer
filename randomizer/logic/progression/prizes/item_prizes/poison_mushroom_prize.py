from __future__ import annotations
from randomizer.data.items.items import (MushroomItem2)
from randomizer.data.physical_objects.bosses import (SPR0219_RED_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (RedMushroomObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class PoisonMushroomPrize(ItemPrize):
    item = MushroomItem2
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject
    _packet_data = (SPR0219_RED_ITEM_COLLECTION, 0)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["PoisonMushroomPrize"]
