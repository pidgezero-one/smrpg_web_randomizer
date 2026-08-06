from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class FireworksItem(RegularItem):
    """Fireworks item class"""
    _item_name: str = "Fireworks"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 172
    _description: str = " A gorgeous\n firework"
    _price: int = 500
    _inflict_type = None


__all__ = ["FireworksItem"]
