from randomizer.data.items.items import (
    CoinTrickItem,
    EarlierTimesItem,
    ExpBoosterItem,
    ScroogeRingItem,
    SeeYaItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH03_FROG_DISCIPLE_SHOP = Shop(
    index=3,
    items=[
        SeeYaItem,
        EarlierTimesItem,
        ExpBoosterItem,
        CoinTrickItem,
        ScroogeRingItem,
    ],
    buy_frog_coin_one=True)


__all__ = ["SH03_FROG_DISCIPLE_SHOP"]
