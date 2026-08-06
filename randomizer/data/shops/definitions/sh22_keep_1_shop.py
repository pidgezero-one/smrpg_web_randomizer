from randomizer.data.items.items import (
    FireCapeItem,
    FireDressItem,
    FirePantsItem,
    FireShellItem,
    FireShirtItem,
    FreshenUpItem,
    MapleSyrupItem,
    MidMushroomItem,
    PickMeUpItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH22_KEEP_1_SHOP = Shop(
    index=22,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        FreshenUpItem,
        FireShirtItem,
        FirePantsItem,
        FireCapeItem,
        FireShellItem,
        FireDressItem,
    ])


__all__ = ["SH22_KEEP_1_SHOP"]
