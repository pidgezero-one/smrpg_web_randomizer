from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SpaceItem2(Weapon):
    """Space item class"""
    _item_name: str = "Space"

    _item_id: int = 4
    _description: str = ""
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _price: int = 0
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(22)


__all__ = ["SpaceItem2"]
