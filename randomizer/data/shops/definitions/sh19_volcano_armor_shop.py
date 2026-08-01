from randomizer.data.items.items import (
    FireCapeItem,
    FireDressItem,
    FirePantsItem,
    FireShellItem,
    FireShirtItem,
)
from smrpgpatchbuilder.datatypes.shops.classes import (Shop)


SH19_VOLCANO_ARMOR_SHOP = Shop(
    index=19,
    items=[
        FireShirtItem,
        FirePantsItem,
        FireCapeItem,
        FireShellItem,
        FireDressItem,
    ])


__all__ = ["SH19_VOLCANO_ARMOR_SHOP"]
