from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SuperSlapItem(Weapon):
    """Super Slap item class"""
    _item_name: str = "Super Slap"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 29
    _description: str = " The Princess'\n mega-slap!"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _attack: int = 70
    _variance: int = 7
    _price: int = 110
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(36)


__all__ = ["SuperSlapItem"]
