from __future__ import annotations
from randomizer.data.items.items import (WalletItem)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class WalletPrize(ItemPrize, KeyPrize):
    item = WalletItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack", description="It looks like it belongs to someone."
    )
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["WalletPrize"]
