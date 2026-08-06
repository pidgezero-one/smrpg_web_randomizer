from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class NauticaDressItem(Armor):
    """NauticaDress item class"""
    _item_name: str = "NauticaDress"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 55
    _description: str = " A female\n sailor's dress"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50
    _inflict_type = None


__all__ = ["NauticaDressItem"]
