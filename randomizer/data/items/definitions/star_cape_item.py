from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class StarCapeItem(Armor):
    """Star Cape item class"""
    _item_name: str = "Star Cape"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 68
    _description: str = " A legendary\n cape."
    _equip_chars: list[PartyCharacter] = [GENO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 100
    _inflict_type = None


__all__ = ["StarCapeItem"]
