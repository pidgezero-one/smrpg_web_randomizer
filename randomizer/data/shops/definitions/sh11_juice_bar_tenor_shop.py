from randomizer.data.items.items import (ElixirItem, FroggieDrinkItem, MegalixirItem)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH11_JUICE_BAR_TENOR_SHOP = Shop(
    index=11,
    items=[
        FroggieDrinkItem,
        ElixirItem,
        MegalixirItem,
    ],
    discount_25=True)


__all__ = ["SH11_JUICE_BAR_TENOR_SHOP"]
