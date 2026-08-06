from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FirePantsItem(Armor):
    """Fire Pants item class"""
    _item_name: str = "Fire Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 62
    _description: str = " Determined\n person's pants"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _inflict_type = None


__all__ = ["FirePantsItem"]
