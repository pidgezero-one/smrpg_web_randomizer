from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SuperHammerItem(Weapon):
    """Super Hammer item class"""
    _item_name: str = "Super Hammer"
    _prefix = ItemPrefix.HAMMER

    _item_id: int = 14
    _description: str = " The standard\n for hammers!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 40
    _variance: int = 4
    _price: int = 70
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(40)
    _perfect_window_ends = UInt8(46)
    _half_time_window_ends = UInt8(50)


__all__ = ["SuperHammerItem"]
