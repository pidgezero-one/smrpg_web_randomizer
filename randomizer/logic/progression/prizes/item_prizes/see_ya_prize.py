from __future__ import annotations
from randomizer.data.items.items import (SeeYaItem)
from randomizer.data.physical_objects.bosses import (SPR0238_STATIC_FROG_COIN_SMALL)
from randomizer.data.physical_objects.items import (FrogCoinItemObject)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class SeeYaPrize(ItemPrize):
    item = SeeYaItem
    _nickname = TreasureHunterNickname(
        nickname="Eject Button", description="Seems useful in a pinch, doesn't\n it?"
    )
    _model = FrogCoinItemObject
    _packet_data = (SPR0238_STATIC_FROG_COIN_SMALL, 0)


__all__ = ["SeeYaPrize"]
