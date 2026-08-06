from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FuzzyCapeItem(Armor):
    """Fuzzy Cape item class"""
    _item_name: str = "Fuzzy Cape"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 59
    _description: str = " A fuzzy cape"
    _equip_chars: list[PartyCharacter] = [GENO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 70
    _inflict_type = None


__all__ = ["FuzzyCapeItem"]
