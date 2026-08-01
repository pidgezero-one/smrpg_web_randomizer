from randomizer.data.items.items import (
    AbleJuiceItem,
    FreshenUpItem,
    FuzzyCapeItem,
    FuzzyDressItem,
    FuzzyPantsItem,
    FuzzyShirtItem,
    HandCannonItem,
    MapleSyrupItem,
    MegaGloveItem,
    MidMushroomItem,
    PickMeUpItem,
    StickyGloveItem,
    WarFanItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH21_NIMBUS_LAND_SHOP = Shop(
    index=21,
    items=[
        MidMushroomItem,
        MapleSyrupItem,
        PickMeUpItem,
        AbleJuiceItem,
        FreshenUpItem,
        MegaGloveItem,
        WarFanItem,
        HandCannonItem,
        StickyGloveItem,
        FuzzyShirtItem,
        FuzzyPantsItem,
        FuzzyCapeItem,
        FuzzyDressItem,
    ])


__all__ = ["SH21_NIMBUS_LAND_SHOP"]
