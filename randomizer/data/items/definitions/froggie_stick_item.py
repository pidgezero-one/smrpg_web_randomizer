from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FroggieStickItem(Weapon):
    """FroggieStick item class"""
    _item_name: str = "FroggieStick"
    _prefix = ItemPrefix.WAND

    _item_id: int = 6
    _description: str = " Frogfucius\n made it"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _attack: int = 20
    _variance: int = 2
    _price: int = 180
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(18)
    _perfect_window_ends = UInt8(24)
    _half_time_window_ends = UInt8(36)


__all__ = ["FroggieStickItem"]
