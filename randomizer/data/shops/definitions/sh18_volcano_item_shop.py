from randomizer.data.items.items import (
    AbleJuiceItem,
    FreshenUpItem,
    MapleSyrupItem,
    MidMushroomItem,
    PickMeUpItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH18_VOLCANO_ITEM_SHOP = Shop(
    index=18,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
    ])


__all__ = ["SH18_VOLCANO_ITEM_SHOP"]
