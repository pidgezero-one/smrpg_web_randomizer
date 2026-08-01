from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HealShellItem(Armor):
    """Heal Shell item class"""
    _item_name: str = "Heal Shell"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 69
    _description: str = " A legendary\n shell."
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 100
    _inflict_type = None

    _remake_name = "Heel Shell"


__all__ = ["HealShellItem"]
