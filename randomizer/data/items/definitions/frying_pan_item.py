from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FryingPanItem(Weapon):
    """Frying Pan item class"""
    _item_name: str = "Frying Pan"
    _prefix = ItemPrefix.FAN

    _item_id: int = 34
    _description: str = " Enough iron to\n be dangerous!"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _attack: int = 90
    _variance: int = 20
    _price: int = 300
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(4)
    _perfect_window_ends = UInt8(10)
    _half_time_window_ends = UInt8(24)


__all__ = ["FryingPanItem"]
