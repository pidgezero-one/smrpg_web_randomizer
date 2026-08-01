from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class WonderChompItem(Weapon):
    """Wonder Chomp item class"""
    _item_name: str = "Wonder Chomp"
    _prefix = ItemPrefix.CHOMP

    _item_id: int = 35
    _description: str = " A powerful,\n studded ball\n and chain"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _attack: int = 67
    _variance: int = 45
    _price: int = 2
    _inflict_type = None
    _half_time_window_begins = UInt8(40)
    _perfect_window_begins = UInt8(50)
    _perfect_window_ends = UInt8(56)
    _half_time_window_ends = UInt8(60)


__all__ = ["WonderChompItem"]
