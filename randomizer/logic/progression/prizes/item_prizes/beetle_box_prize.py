from __future__ import annotations
from randomizer.data.items.items import (BeetleBoxItem)
from randomizer.data.physical_objects.items import (BeetleObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize)


class BeetleBoxPrize(ItemPrize):
    item = BeetleBoxItem
    _model = BeetleObject
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["BeetleBoxPrize"]
