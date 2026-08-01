from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class MarioDollItem(RegularItem):
    """Mario Doll item class"""
    _item_name: str = "Mario Doll"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 133
    _description: str = " It's an\n action figure"
    _price: int = 0

    _inflict_type = None


__all__ = ["MarioDollItem"]
