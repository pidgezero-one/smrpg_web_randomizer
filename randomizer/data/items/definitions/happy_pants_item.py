from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HappyPantsItem(Armor):
    """Happy Pants item class"""
    _item_name: str = "Happy Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 48
    _description: str = " A lucky\n pair of pants"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38
    _inflict_type = None


__all__ = ["HappyPantsItem"]
