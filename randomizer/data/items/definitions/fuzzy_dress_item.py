from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FuzzyDressItem(Armor):
    """Fuzzy Dress item class"""
    _item_name: str = "Fuzzy Dress"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 60
    _description: str = " A fuzzy dress"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70
    _inflict_type = None


__all__ = ["FuzzyDressItem"]
