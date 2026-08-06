from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class BeetleBoxItem(RegularItem):
    """Beetle Box item class"""
    _item_name: str = "Beetle Box"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 146
    _description: str = " It's an insect\n cage"
    _price: int = 0
    _inflict_type = None


__all__ = ["BeetleBoxItem"]
