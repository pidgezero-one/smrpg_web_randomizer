from randomizer.data.items.items import (
    AbleJuiceItem,
    HoneySyrupItem,
    MushroomItem,
    PickMeUpItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH01_ROSE_TOWN_ITEM_SHOP = Shop(
    index=1,
    items=[
        MushroomItem,
        HoneySyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
    ])


__all__ = ["SH01_ROSE_TOWN_ITEM_SHOP"]
