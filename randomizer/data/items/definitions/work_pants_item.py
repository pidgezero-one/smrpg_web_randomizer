from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
    GENO,
    MALLOW,
    MARIO,
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class WorkPantsItem(Armor):
    """Work Pants item class"""
    _item_name: str = "Work Pants"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 45
    _description: str = " Sweaty\n work pants!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = 5
    _attack: int = 10
    _defense: int = 15
    _magic_attack: int = 10
    _magic_defense: int = 5
    _price: int = 22
    _inflict_type = None


__all__ = ["WorkPantsItem"]
