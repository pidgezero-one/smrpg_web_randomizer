from __future__ import annotations
from randomizer.data.items.items import (RareFrogCoinItem)
from randomizer.data.physical_objects.bosses import (SPR0238_STATIC_FROG_COIN_SMALL)
from randomizer.data.physical_objects.items import (SmallFrogCoinObjectNoMoney)
from randomizer.types.prize import (FortuneEnum, ItemPrize, KeyPrize, TreasureHunterNickname)


class RareFrogCoinPrize(ItemPrize, KeyPrize):
    item = RareFrogCoinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Coin", description="It looks different from most Frog \nCoins."
    )
    _model = SmallFrogCoinObjectNoMoney
    _packet_data = (SPR0238_STATIC_FROG_COIN_SMALL, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE


__all__ = ["RareFrogCoinPrize"]
