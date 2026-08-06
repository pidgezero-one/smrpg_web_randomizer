from randomizer.data.items.items import (
    BtubRingItem,
    ChompShellItem,
    HandGunItem,
    HappyCapeItem,
    HappyPantsItem,
    HappyShellItem,
    HappyShirtItem,
    MapleSyrupItem,
    MidMushroomItem,
    SuperHammerItem,
    WhompGloveItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH05_MARRYMORE_SHOP = Shop(
    index=5,
    items=[
        SuperHammerItem,
        HandGunItem,
        WhompGloveItem,
        ChompShellItem,
        HappyShirtItem,
        HappyPantsItem,
        HappyCapeItem,
        HappyShellItem,
        BtubRingItem,
        MidMushroomItem,
        MapleSyrupItem,
    ])


__all__ = ["SH05_MARRYMORE_SHOP"]
