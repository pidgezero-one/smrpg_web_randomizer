from __future__ import annotations
from randomizer.data.items.items import (RottenMushItem)
from randomizer.data.physical_objects.bosses import (SPR0222_BANANA_PEEL)
from randomizer.data.physical_objects.items import (BananaObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RottenMushPrize(ItemPrize):
    item = RottenMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject
    _packet_data = (SPR0222_BANANA_PEEL, 0)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["RottenMushPrize"]
