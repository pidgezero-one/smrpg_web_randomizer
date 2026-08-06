from randomizer.data.items.items import (
    HappyCapeItem,
    HappyPantsItem,
    HappyShellItem,
    HappyShirtItem,
    MegaCapeItem,
    MegaPantsItem,
    MegaShirtItem,
    NauticaDressItem,
    PantsItem,
    SailorCapeItem,
    SailorPantsItem,
    SailorShirtItem,
    ShirtItem,
    ThickPantsItem,
    ThickShirtItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH14_SEASIDE_ARMOR_SHOP = Shop(
    index=14,
    items=[
        SailorShirtItem,
        SailorPantsItem,
        SailorCapeItem,
        NauticaDressItem,
        ShirtItem,
        PantsItem,
        ThickShirtItem,
        ThickPantsItem,
        MegaShirtItem,
        MegaPantsItem,
        MegaCapeItem,
        HappyShirtItem,
        HappyPantsItem,
        HappyCapeItem,
        HappyShellItem,
    ])


__all__ = ["SH14_SEASIDE_ARMOR_SHOP"]
