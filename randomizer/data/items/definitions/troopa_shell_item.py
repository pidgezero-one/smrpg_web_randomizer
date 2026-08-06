from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class TroopaShellItem(Weapon):
    """Troopa Shell item class"""
    _item_name: str = "Troopa Shell"
    _prefix = ItemPrefix.SHELL

    _item_id: int = 18
    _description: str = " Kick with it!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 5
    _price: int = 90
    _inflict_type = None
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)

    _remake_name = "Para Shell"


__all__ = ["TroopaShellItem"]
