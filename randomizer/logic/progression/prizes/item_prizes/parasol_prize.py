from __future__ import annotations
from randomizer.data.items.items import (ParasolItem)
from randomizer.data.physical_objects.items import (ParasolObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class ParasolPrize(ItemPrize):
    item = ParasolItem
    _nickname = TreasureHunterNickname(
        nickname="Umbrella", description="There's no turtle inside of it."
    )
    _model = ParasolObject
    _fortune_type: FortuneEnum = FortuneEnum.WEAPON


__all__ = ["ParasolPrize"]
