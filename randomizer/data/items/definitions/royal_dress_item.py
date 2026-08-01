from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class RoyalDressItem(Armor):
    """Royal Dress item class"""
    _item_name: str = "Royal Dress"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 70
    _description: str = " A legendary\n dress!"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100
    _inflict_type = None


__all__ = ["RoyalDressItem"]
