from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class DummyItem(RegularItem):
    """Placeholder item for unused item IDs"""
    _item_name: str = "--------"
    _prefix = ItemPrefix.EMPTY_SPACE
    _description: str = ""
    _price: int = 0
    _inflict_type = None

    def __init__(self, item_id: int):
        self._item_id = item_id
        super().__init__()


__all__ = ["DummyItem"]
