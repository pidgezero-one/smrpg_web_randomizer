from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class SeedItem(RegularItem):
    """Seed item class"""
    _item_name: str = "Seed"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 158
    _description: str = " A fast-growing\n seed"
    _price: int = 0
    _inflict_type = None


__all__ = ["SeedItem"]
