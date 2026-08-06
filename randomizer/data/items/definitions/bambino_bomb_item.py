from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class BambinoBombItem(RegularItem):
    """Bambino Bomb item class"""
    _item_name: str = "Bambino Bomb"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 135
    _description: str = " Handle with\n care!"
    _price: int = 0
    _inflict_type = None

    _remake_name = "Microbomb"


__all__ = ["BambinoBombItem"]
