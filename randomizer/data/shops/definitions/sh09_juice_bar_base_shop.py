from randomizer.data.items.items import (FroggieDrinkItem)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH09_JUICE_BAR_BASE_SHOP = Shop(
    index=9,
    items=[
        FroggieDrinkItem,
    ])


__all__ = ["SH09_JUICE_BAR_BASE_SHOP"]
