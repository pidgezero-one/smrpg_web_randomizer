from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HappyCapeItem(Armor):
    """Happy Cape item class"""
    _item_name: str = "Happy Cape"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 49
    _description: str = " A lucky cape"
    _equip_chars: list[PartyCharacter] = [GENO]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 38
    _inflict_type = None


__all__ = ["HappyCapeItem"]
