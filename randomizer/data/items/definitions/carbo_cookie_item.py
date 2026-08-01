from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class CarboCookieItem(RegularItem):
    """Carbo Cookie item class"""
    _item_name: str = "Carbo Cookie"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 137
    _description: str = " Kid's love 'em"
    _price: int = 2
    _inflict_type = None


__all__ = ["CarboCookieItem"]
