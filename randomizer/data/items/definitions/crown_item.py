from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CrownItem(RegularItem):
    """Crown item class"""
    _item_name: str = "Crown"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 170
    _description: str = " A fancy crown!"
    _price: int = 0
    _inflict_type = None


__all__ = ["CrownItem"]
