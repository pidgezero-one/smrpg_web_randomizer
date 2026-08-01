from __future__ import annotations
from randomizer.data.items.items import (ShirtItem)
from randomizer.data.physical_objects.bosses import (SPR0230_OVERALLS)
from randomizer.data.physical_objects.items import (OverallsObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class ShirtPrize(ItemPrize):
    item = ShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Overalls", description="Don't go to work without 'em!"
    )
    _fortune_type: FortuneEnum = FortuneEnum.ARMOR
    _model = OverallsObject
    _packet_data = (SPR0230_OVERALLS, 0)


__all__ = ["ShirtPrize"]
