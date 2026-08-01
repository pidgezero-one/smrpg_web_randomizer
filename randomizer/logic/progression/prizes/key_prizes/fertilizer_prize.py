from __future__ import annotations
from randomizer.data.items.items import (FertilizerItem)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class FertilizerPrize(ItemPrize, KeyPrize):
    item = FertilizerItem
    _nickname = TreasureHunterNickname(
        nickname="Bag of Dirt",
        description="It seems different from the soil\n I dug it out of.",
    )
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["FertilizerPrize"]
