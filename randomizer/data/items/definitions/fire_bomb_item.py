from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class FireBombItem(RegularItem):
    """Fire Bomb item class"""
    _item_name: str = "Fire Bomb"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Fire Bomb........."

    _item_id: int = 113
    _description: str = " Hit all\n enemies w/fire"
    _inflict: int = 120
    _price: int = 200
    _inflict_type = None
    _inflict_element = Element.FIRE
    _usable_battle: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True


__all__ = ["FireBombItem"]
