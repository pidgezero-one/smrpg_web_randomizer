from __future__ import annotations
from randomizer.data.items.items import (SleepyBombItem)
from randomizer.data.physical_objects.bosses import (SPR0221_YELLOW_ITEM_COLLECTION)
from randomizer.data.physical_objects.items import (YellowBombObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class SleepyBombPrize(ItemPrize):
    item = SleepyBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = YellowBombObject
    _packet_data = (SPR0221_YELLOW_ITEM_COLLECTION, 10)


__all__ = ["SleepyBombPrize"]
