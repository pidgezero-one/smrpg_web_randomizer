from __future__ import annotations
from randomizer.data.items.items import (RoyalSyrupItem)
from randomizer.data.physical_objects.bosses import (SPR0221_YELLOW_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (YellowSyrupObject)
from randomizer.types.prize import (FortuneEnum, ItemPrize, TreasureHunterNickname)


class RoyalSyrupPrize(ItemPrize):
    item = RoyalSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = YellowSyrupObject
    _packet_data = (SPR0221_YELLOW_ITEM_COLLECTION, 1)
    _fortune_type: FortuneEnum = FortuneEnum.SNACK


__all__ = ["RoyalSyrupPrize"]
