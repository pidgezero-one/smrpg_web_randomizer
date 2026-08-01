from randomizer.data.items.items import (
    AntidotePinItem,
    FearlessPinItem,
    JumpShoesItem,
    ThickPantsItem,
    ThickShirtItem,
    TrueformPinItem,
    WakeUpPinItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH02_ROSE_TOWN_ARMOR_SHOP = Shop(
    index=2,
    items=[
        ThickShirtItem,
        ThickPantsItem,
        JumpShoesItem,
        AntidotePinItem,
        WakeUpPinItem,
        TrueformPinItem,
        FearlessPinItem,
    ])


__all__ = ["SH02_ROSE_TOWN_ARMOR_SHOP"]
