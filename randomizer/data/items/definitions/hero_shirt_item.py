from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HeroShirtItem(Armor):
    """Hero Shirt item class"""
    _item_name: str = "Hero Shirt"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 66
    _description: str = " A legendary\n shirt."
    _equip_chars: list[PartyCharacter] = [MARIO]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100
    _inflict_type = None


__all__ = ["HeroShirtItem"]
