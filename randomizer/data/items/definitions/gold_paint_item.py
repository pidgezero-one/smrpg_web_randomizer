from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class GoldPaintItem(RegularItem):
    """Gold Paint item class"""
    _item_name: str = "Gold Paint"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 164
    _description: str = " Garro\n uses it"
    _price: int = 0
    _inflict_type = None


__all__ = ["GoldPaintItem"]
