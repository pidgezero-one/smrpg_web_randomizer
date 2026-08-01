from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SpaceItem(Weapon):
    """Space item class"""
    _item_name: str = "Space"

    _item_id: int = 3
    _description: str = ""
    _equip_chars: list[PartyCharacter] = [GENO]
    _price: int = 0
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(56)


__all__ = ["SpaceItem"]
