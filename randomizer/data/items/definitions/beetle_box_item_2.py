from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class BeetleBoxItem2(RegularItem):
    """Beetle Box item class"""
    _item_name: str = "Beetle Box"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 147
    _description: str = " There are\n beetles inside"
    _price: int = 0
    _inflict_type = None


__all__ = ["BeetleBoxItem2"]
