from randomizer.data.items.items import (
    BracerItem,
    CrystallineItem,
    EnergizerItem,
    PowerBlastItem,
    SleepyBombItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH06_FROG_COIN_EMPORIUM_SHOP = Shop(
    index=6,
    items=[
        SleepyBombItem,
        BracerItem,
        EnergizerItem,
        CrystallineItem,
        PowerBlastItem,
    ],
    buy_frog_coin=True)


__all__ = ["SH06_FROG_COIN_EMPORIUM_SHOP"]
