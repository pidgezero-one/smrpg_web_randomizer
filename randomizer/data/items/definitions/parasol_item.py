from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class ParasolItem(Weapon):
    """Parasol item class"""
    _item_name: str = "Parasol"
    _prefix = ItemPrefix.WAND

    _item_id: int = 19
    _description: str = " Inflicts\n serious pain!"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _attack: int = 50
    _variance: int = 5
    _price: int = 84
    _inflict_type = None
    _half_time_window_begins = UInt8(5)
    _perfect_window_begins = UInt8(8)
    _perfect_window_ends = UInt8(14)
    _half_time_window_ends = UInt8(24)


__all__ = ["ParasolItem"]
