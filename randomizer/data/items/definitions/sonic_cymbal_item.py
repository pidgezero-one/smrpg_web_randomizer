from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SonicCymbalItem(Weapon):
    """Sonic Cymbal item class"""
    _item_name: str = "Sonic Cymbal"
    _prefix = ItemPrefix.MUSIC

    _item_id: int = 32
    _description: str = " Puts noise to\n work for you!"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _attack: int = 70
    _variance: int = 7
    _price: int = 108
    _inflict_type = None
    _half_time_window_begins = UInt8(4)
    _perfect_window_begins = UInt8(5)
    _perfect_window_ends = UInt8(11)
    _half_time_window_ends = UInt8(30)


__all__ = ["SonicCymbalItem"]
