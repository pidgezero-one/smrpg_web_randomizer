from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FuzzyShirtItem(Armor):
    """Fuzzy Shirt item class"""
    _item_name: str = "Fuzzy Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 57
    _description: str = " A fuzzy shirt"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70
    _inflict_type = None


__all__ = ["FuzzyShirtItem"]
