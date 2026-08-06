from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HappyShellItem(Armor):
    """Happy Shell item class"""
    _item_name: str = "Happy Shell"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 50
    _description: str = " A lucky shell"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 38
    _inflict_type = None


__all__ = ["HappyShellItem"]
