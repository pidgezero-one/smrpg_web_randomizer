from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FireDressItem(Armor):
    """Fire Dress item class"""
    _item_name: str = "Fire Dress"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 65
    _description: str = " Determined\n woman's dress"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _inflict_type = None


__all__ = ["FireDressItem"]
