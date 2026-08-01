from randomizer.data.items.items import (
    AbleJuiceItem,
    FreshenUpItem,
    HoneySyrupItem,
    MapleSyrupItem,
    MidMushroomItem,
    MushroomItem,
    PickMeUpItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH16_SEASIDE_HEALTH_FOOD_SHOP = Shop(
    index=16,
    items=[
        MushroomItem,
        MidMushroomItem,
        HoneySyrupItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])


__all__ = ["SH16_SEASIDE_HEALTH_FOOD_SHOP"]
