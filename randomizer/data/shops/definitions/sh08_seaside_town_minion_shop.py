from randomizer.data.items.items import (
    BadMushroomItem,
    FireBombItem,
    FrightBombItem,
    IceBombItem,
    MukuCookieItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH08_SEASIDE_TOWN_MINION_SHOP = Shop(
    index=8,
    items=[
        BadMushroomItem,
        MukuCookieItem,
        FrightBombItem,
        FireBombItem,
        IceBombItem,
    ])


__all__ = ["SH08_SEASIDE_TOWN_MINION_SHOP"]
