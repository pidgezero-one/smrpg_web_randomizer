from __future__ import annotations
from randomizer.data.items.items import (SailorShirtItem)
from randomizer.data.physical_objects.bosses import (SPR0230_OVERALLS)
from randomizer.data.physical_objects.items import (OverallsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class SailorShirtPrize(ItemPrize):
    item = SailorShirtItem
    _nickname = TreasureHunterNickname(
        nickname="White Overalls", description="Built for life on the sea."
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = OverallsObject
    _packet_data = (SPR0230_OVERALLS, 0)


__all__ = ["SailorShirtPrize"]
