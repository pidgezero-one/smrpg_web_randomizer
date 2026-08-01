from __future__ import annotations
from randomizer.data.items.items import (EarlierTimesItem)
from randomizer.data.physical_objects.bosses import (SPR0238_STATIC_FROG_COIN_SMALL)
from randomizer.data.physical_objects.items import (FrogCoinItemObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class EarlierTimesPrize(ItemPrize):
    item = EarlierTimesItem
    _nickname = TreasureHunterNickname(
        nickname="Reset Button", description="Sounds useful in a pinch, doesn't\n it?"
    )
    _model = FrogCoinItemObject
    _packet_data = (SPR0238_STATIC_FROG_COIN_SMALL, 0)


__all__ = ["EarlierTimesPrize"]
