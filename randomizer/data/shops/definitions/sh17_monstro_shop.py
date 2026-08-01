from randomizer.data.items.items import (
    AbleJuiceItem,
    CourageShellItem,
    FreshenUpItem,
    MapleSyrupItem,
    MidMushroomItem,
    PickMeUpItem,
    SpikedLinkItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH17_MONSTRO_SHOP = Shop(
    index=17,
    items=[
        SpikedLinkItem,
        CourageShellItem,
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])


__all__ = ["SH17_MONSTRO_SHOP"]
