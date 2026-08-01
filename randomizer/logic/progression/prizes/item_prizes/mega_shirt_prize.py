from __future__ import annotations
from randomizer.data.items.items import (MegaShirtItem)
from randomizer.data.physical_objects.bosses import (SPR0230_OVERALLS)
from randomizer.data.physical_objects.items import (OverallsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class MegaShirtPrize(ItemPrize):
    item = MegaShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = OverallsObject
    _packet_data = (SPR0230_OVERALLS, 0)


__all__ = ["MegaShirtPrize"]
