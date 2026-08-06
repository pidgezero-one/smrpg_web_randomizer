from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)


class RockCandyItem(RegularItem):
    """Rock Candy item class"""
    _item_name: str = "Rock Candy"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Rock Candy......."

    _item_id: int = 131
    _description: str = " Attack all\n enemies"
    _inflict: int = 200
    _price: int = 400
    _inflict_type = None
    _usable_battle: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["RockCandyItem"]
