from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class CourageShellItem(Armor):
    """CourageShell item class"""
    _item_name: str = "CourageShell"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 56
    _description: str = " A stout shell"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 60
    _inflict_type = None


__all__ = ["CourageShellItem"]
