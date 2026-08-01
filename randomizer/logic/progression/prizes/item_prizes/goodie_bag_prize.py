from __future__ import annotations
from randomizer.data.items.items import (GoodieBagItem)
from randomizer.types.prize import (ItemPrize, TreasureHunterNickname)


class GoodieBagPrize(ItemPrize):
    item = GoodieBagItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack", description="It could make you rich!"
    )


__all__ = ["GoodieBagPrize"]
