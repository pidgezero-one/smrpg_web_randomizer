from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class PrincePantsItem(Armor):
    """Prince Pants item class"""
    _item_name: str = "Prince Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 67
    _description: str = " Legendary\n pants!"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100
    _inflict_type = None


__all__ = ["PrincePantsItem"]
