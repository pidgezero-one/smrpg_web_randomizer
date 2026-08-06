from randomizer.data.items.items import (ElixirItem, FroggieDrinkItem)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH10_JUICE_BAR_ALTO_SHOP = Shop(
    index=10,
    items=[
        FroggieDrinkItem,
        ElixirItem,
    ],
    discount_12=True)


__all__ = ["SH10_JUICE_BAR_ALTO_SHOP"]
