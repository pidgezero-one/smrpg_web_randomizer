from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class MegaPantsItem(Armor):
    """Mega Pants item class"""
    _item_name: str = "Mega Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 44
    _description: str = " Durable work\n pants"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 22
    _inflict_type = None


__all__ = ["MegaPantsItem"]
