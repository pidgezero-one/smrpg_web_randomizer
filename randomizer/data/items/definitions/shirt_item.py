from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class ShirtItem(Armor):
    """Shirt item class"""
    _item_name: str = "Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 39
    _description: str = " It's a\n shirt!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 6
    _magic_defense: int = 6
    _price: int = 7
    _inflict_type = None


__all__ = ["ShirtItem"]
