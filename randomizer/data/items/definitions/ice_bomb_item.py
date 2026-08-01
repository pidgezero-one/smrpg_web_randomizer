from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class IceBombItem(RegularItem):
    """Ice Bomb item class"""
    _item_name: str = "Ice Bomb"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Ice Bomb.........."

    _item_id: int = 114
    _description: str = " Hit all\n enemies w/ice"
    _inflict: int = 140
    _price: int = 250
    _inflict_type = None
    _inflict_element = Element.ICE
    _usable_battle: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["IceBombItem"]
