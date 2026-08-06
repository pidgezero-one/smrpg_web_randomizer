from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class ChompShellItem(Weapon):
    """Chomp Shell item class"""
    _item_name: str = "Chomp Shell"
    _prefix = ItemPrefix.CHOMP

    _item_id: int = 13
    _description: str = " It's a\n Kinklink shell"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _attack: int = 9
    _variance: int = 3
    _price: int = 60
    _inflict_type = None
    _half_time_window_begins = UInt8(40)
    _perfect_window_begins = UInt8(50)
    _perfect_window_ends = UInt8(56)
    _half_time_window_ends = UInt8(60)

    _remake_name = "Fake Chomp"


__all__ = ["ChompShellItem"]
