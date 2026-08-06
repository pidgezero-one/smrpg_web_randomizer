from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class LazyShellItem(Weapon):
    """Lazy Shell item class"""
    _item_name: str = "Lazy Shell"
    _prefix = ItemPrefix.SHELL

    _item_id: int = 33
    _description: str = " Toss a shell\n at an enemy!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 90
    _variance: int = 40
    _price: int = 200
    _inflict_type = None
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)


__all__ = ["LazyShellItem"]
