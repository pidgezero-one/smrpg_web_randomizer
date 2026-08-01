from randomizer.data.items.items import (
    AbleJuiceItem,
    FreshenUpItem,
    HandGunItem,
    HurlyGlovesItem,
    MapleSyrupItem,
    MidMushroomItem,
    NauticaDressItem,
    PickMeUpItem,
    SailorCapeItem,
    SailorPantsItem,
    SailorShirtItem,
    SuperHammerItem,
    WhompGloveItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH07_SEA_AND_SHIP_SHAMAN_SHOP = Shop(
    index=7,
    items=[
        HurlyGlovesItem,
        SuperHammerItem,
        HandGunItem,
        WhompGloveItem,
        SailorShirtItem,
        SailorPantsItem,
        SailorCapeItem,
        NauticaDressItem,
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])


__all__ = ["SH07_SEA_AND_SHIP_SHAMAN_SHOP"]
