from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FireCapeItem(Armor):
    """Fire Cape item class"""
    _item_name: str = "Fire Cape"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 63
    _description: str = " Determined\n person's cape"
    _equip_chars: list[PartyCharacter] = [GENO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 90
    _inflict_type = None


__all__ = ["FireCapeItem"]
