from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class WarFanItem(Weapon):
    """War Fan item class"""
    _item_name: str = "War Fan"
    _prefix = ItemPrefix.FAN

    _item_id: int = 25
    _description: str = " A mysterious\n battle fan!"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _attack: int = 60
    _variance: int = 6
    _price: int = 100
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(2)
    _perfect_window_ends = UInt8(8)
    _half_time_window_ends = UInt8(22)


__all__ = ["WarFanItem"]
