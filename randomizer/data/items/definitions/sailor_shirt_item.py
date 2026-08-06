from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SailorShirtItem(Armor):
    """Sailor Shirt item class"""
    _item_name: str = "Sailor Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 52
    _description: str = " A sailor's\n suit"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50
    _inflict_type = None


__all__ = ["SailorShirtItem"]
