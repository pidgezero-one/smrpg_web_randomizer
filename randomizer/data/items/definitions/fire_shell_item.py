from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FireShellItem(Armor):
    """Fire Shell item class"""
    _item_name: str = "Fire Shell"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 64
    _description: str = " Determined\n person's shell"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 90
    _inflict_type = None


__all__ = ["FireShellItem"]
