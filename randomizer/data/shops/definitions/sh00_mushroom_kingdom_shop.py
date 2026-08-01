from randomizer.data.items.items import (
    AbleJuiceItem,
    AntidotePinItem,
    HoneySyrupItem,
    JumpShoesItem,
    MushroomItem,
    PantsItem,
    PickMeUpItem,
    ShirtItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH00_MUSHROOM_KINGDOM_SHOP = Shop(
    index=0,
    items=[
        MushroomItem,
        HoneySyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        ShirtItem,
        PantsItem,
        JumpShoesItem,
        AntidotePinItem,
    ])


__all__ = ["SH00_MUSHROOM_KINGDOM_SHOP"]
