from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class ThickShirtItem(Armor):
    """Thick Shirt item class"""
    _item_name: str = "Thick Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 41
    _description: str = " A padded shirt"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 12
    _magic_defense: int = 8
    _price: int = 14
    _inflict_type = None


__all__ = ["ThickShirtItem"]
