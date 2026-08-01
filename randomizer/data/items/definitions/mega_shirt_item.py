from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class MegaShirtItem(Armor):
    """Mega Shirt item class"""
    _item_name: str = "Mega Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 43
    _description: str = " Durable stay-\n pressed shirt"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 18
    _magic_defense: int = 10
    _price: int = 22
    _inflict_type = None


__all__ = ["MegaShirtItem"]
