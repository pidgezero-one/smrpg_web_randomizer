from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HappyShirtItem(Armor):
    """Happy Shirt item class"""
    _item_name: str = "Happy Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 47
    _description: str = " A lucky shirt"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38
    _inflict_type = None


__all__ = ["HappyShirtItem"]
