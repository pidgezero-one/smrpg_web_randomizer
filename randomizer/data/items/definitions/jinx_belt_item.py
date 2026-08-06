from randomizer.types.item import (Accessory)
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


class JinxBeltItem(Accessory):
    """Jinx Belt item class"""
    _item_name: str = "Jinx Belt"
    _prefix = ItemPrefix.RING

    _item_id: int = 90
    _description: str = " Jinx's emblem\n of power!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = 12
    _attack: int = 27
    _defense: int = 27
    _price: int = 1998
    _inflict_type = None
    _prevent_ko: bool = True


__all__ = ["JinxBeltItem"]
