from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class ThickPantsItem(Armor):
    """Thick Pants item class"""
    _item_name: str = "Thick Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 42
    _description: str = " Padded pants"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 14
    _inflict_type = None


__all__ = ["ThickPantsItem"]
