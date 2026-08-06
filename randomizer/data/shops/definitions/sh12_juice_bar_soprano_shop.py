from randomizer.data.items.items import (
    ElixirItem,
    FroggieDrinkItem,
    KerokeroColaItem,
    MegalixirItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH12_JUICE_BAR_SOPRANO_SHOP = Shop(
    index=12,
    items=[
        FroggieDrinkItem,
        ElixirItem,
        MegalixirItem,
        KerokeroColaItem,
    ],
    discount_50=True)


__all__ = ["SH12_JUICE_BAR_SOPRANO_SHOP"]
