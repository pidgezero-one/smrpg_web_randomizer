from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class NokNokShellItem(Weapon):
    """NokNok Shell item class"""
    _item_name: str = "NokNok Shell"
    _prefix = ItemPrefix.SHELL

    _item_id: int = 7
    _description: str = " Kick to attack"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 20
    _variance: int = 2
    _price: int = 20
    _inflict_type = None
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)

    _remake_name = "Koopa Shell"


__all__ = ["NokNokShellItem"]
