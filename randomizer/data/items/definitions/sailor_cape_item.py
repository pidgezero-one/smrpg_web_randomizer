from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SailorCapeItem(Armor):
    """Sailor Cape item class"""
    _item_name: str = "Sailor Cape"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 54
    _description: str = " A sailor's\n cape"
    _equip_chars: list[PartyCharacter] = [GENO]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 50
    _inflict_type = None


__all__ = ["SailorCapeItem"]
