from randomizer.data.items.items import (
    AbleJuiceItem,
    FreshenUpItem,
    FroggieDrinkItem,
    MapleSyrupItem,
    MaxMushroomItem,
    MidMushroomItem,
    PickMeUpItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH24_FACTORY_TOAD_SHOP = Shop(
    index=24,
    items=[
        MidMushroomItem,
        MaxMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
        FroggieDrinkItem,
    ],
    discount_50=True)


__all__ = ["SH24_FACTORY_TOAD_SHOP"]
