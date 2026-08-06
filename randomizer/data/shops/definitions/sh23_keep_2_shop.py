from randomizer.data.items.items import (
    FreshenUpItem,
    HealShellItem,
    HeroShirtItem,
    MapleSyrupItem,
    MidMushroomItem,
    PickMeUpItem,
    PrincePantsItem,
    RoyalDressItem,
    StarCapeItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH23_KEEP_2_SHOP = Shop(
    index=23,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        FreshenUpItem,
        HeroShirtItem,
        PrincePantsItem,
        StarCapeItem,
        HealShellItem,
        RoyalDressItem,
    ])


__all__ = ["SH23_KEEP_2_SHOP"]
