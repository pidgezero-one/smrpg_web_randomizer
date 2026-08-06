from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HammerItem(Weapon):
    """Hammer item class"""
    _item_name: str = "Hammer"
    _prefix = ItemPrefix.HAMMER

    _item_id: int = 5
    _description: str = " Pounds enemies"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 10
    _variance: int = 1
    _price: int = 70
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(14)
    _perfect_window_ends = UInt8(20)
    _half_time_window_ends = UInt8(38)


__all__ = ["HammerItem"]
