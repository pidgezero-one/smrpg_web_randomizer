from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class MegaCapeItem(Armor):
    """Mega Cape item class"""
    _item_name: str = "Mega Cape"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 46
    _description: str = " Durable\n pressed cape"
    _equip_chars: list[PartyCharacter] = [GENO]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 22
    _inflict_type = None


__all__ = ["MegaCapeItem"]
