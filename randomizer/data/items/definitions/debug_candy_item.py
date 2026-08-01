from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class DebugCandyItem(RegularItem):
    """Debug Candy — reusable Rock Candy for debug/testing.

    Same effect as Rock Candy (200 power, all enemies) but ``_reusable``
    is True so it never decrements from inventory. Lives at item_id 177
    (first slot in the contiguous DummyItem range, safely past every
    real vanilla item ID) and is intended only for debug builds.
    """
    _item_name: str = "Debug Candy"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Debug Candy......"

    _item_id: int = 177
    _description: str = " Attack all\n enemies\n (reusable)"
    _inflict: int = 200
    _price: int = 1998
    _inflict_type = None
    _usable_battle: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _reusable: bool = True
    _no_sell: bool = True


__all__ = ["DebugCandyItem"]
