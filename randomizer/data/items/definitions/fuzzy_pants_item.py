from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FuzzyPantsItem(Armor):
    """Fuzzy Pants item class"""
    _item_name: str = "Fuzzy Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 58
    _description: str = " Fuzzy pants"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70
    _inflict_type = None


__all__ = ["FuzzyPantsItem"]
