from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class PantsItem(Armor):
    """Pants item class"""
    _item_name: str = "Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 40
    _description: str = " It's a pair\n of pants!"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 7
    _inflict_type = None


__all__ = ["PantsItem"]
