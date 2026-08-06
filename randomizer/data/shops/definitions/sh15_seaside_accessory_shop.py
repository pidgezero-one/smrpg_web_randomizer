from randomizer.data.items.items import (
    AntidotePinItem,
    FearlessPinItem,
    JumpShoesItem,
    TrueformPinItem,
    WakeUpPinItem,
    ZoomShoesItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH15_SEASIDE_ACCESSORY_SHOP = Shop(
    index=15,
    items=[
        JumpShoesItem,
        AntidotePinItem,
        WakeUpPinItem,
        FearlessPinItem,
        TrueformPinItem,
        ZoomShoesItem,
    ])


__all__ = ["SH15_SEASIDE_ACCESSORY_SHOP"]
