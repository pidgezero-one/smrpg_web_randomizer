from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class DoublePunchItem(Weapon):
    """Double Punch item class"""
    _item_name: str = "Double Punch"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 21
    _description: str = " A handy double\n rocket punch"
    _equip_chars: list[PartyCharacter] = [GENO]
    _attack: int = 35
    _variance: int = 5
    _price: int = 88
    _inflict_type = None
    _half_time_window_begins = UInt8(6)
    _perfect_window_begins = UInt8(26)
    _perfect_window_ends = UInt8(32)
    _half_time_window_ends = UInt8(36)


__all__ = ["DoublePunchItem"]
