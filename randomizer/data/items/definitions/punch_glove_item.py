from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class PunchGloveItem(Weapon):
    """Punch Glove item class"""
    _item_name: str = "Punch Glove"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 8
    _description: str = " Knock out\n power!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 30
    _variance: int = 3
    _price: int = 36
    _inflict_type = None
    _half_time_window_begins = UInt8(4)
    _perfect_window_begins = UInt8(8)
    _perfect_window_ends = UInt8(14)
    _half_time_window_ends = UInt8(22)


__all__ = ["PunchGloveItem"]
