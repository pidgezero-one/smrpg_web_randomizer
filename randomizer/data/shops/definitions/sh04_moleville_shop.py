from randomizer.data.items.items import (
    CymbalsItem,
    FingerShotItem,
    MapleSyrupItem,
    MegaCapeItem,
    MegaPantsItem,
    MegaShirtItem,
    MidMushroomItem,
    PunchGloveItem,
    WorkPantsItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH04_MOLEVILLE_SHOP = Shop(
    index=4,
    items=[
        PunchGloveItem,
        FingerShotItem,
        CymbalsItem,
        MegaShirtItem,
        MegaCapeItem,
        MegaPantsItem,
        WorkPantsItem,
        MidMushroomItem,
        MapleSyrupItem,
    ])


__all__ = ["SH04_MOLEVILLE_SHOP"]
