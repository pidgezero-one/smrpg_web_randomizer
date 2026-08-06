from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FireShirtItem(Armor):
    """Fire Shirt item class"""
    _item_name: str = "Fire Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 61
    _description: str = " Determined\n person's shirt"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _inflict_type = None


__all__ = ["FireShirtItem"]
