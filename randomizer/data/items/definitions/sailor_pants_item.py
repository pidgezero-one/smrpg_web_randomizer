from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SailorPantsItem(Armor):
    """Sailor Pants item class"""
    _item_name: str = "Sailor Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 53
    _description: str = " A sailor's\n pants"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50
    _inflict_type = None


__all__ = ["SailorPantsItem"]
