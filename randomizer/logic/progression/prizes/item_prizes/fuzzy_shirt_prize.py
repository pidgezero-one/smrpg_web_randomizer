from __future__ import annotations
from randomizer.data.items.items import (FuzzyShirtItem)
from randomizer.data.physical_objects.bosses import (SPR0230_OVERALLS)
from randomizer.data.physical_objects.items import (OverallsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class FuzzyShirtPrize(ItemPrize):
    item = FuzzyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Green Overalls", description="Made of the finest fleece."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = OverallsObject
    _packet_data = (SPR0230_OVERALLS, 0)


__all__ = ["FuzzyShirtPrize"]
