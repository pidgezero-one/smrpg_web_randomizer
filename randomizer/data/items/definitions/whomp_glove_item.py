from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class WhompGloveItem(Weapon):
    """Whomp Glove item class"""
    _item_name: str = "Whomp Glove"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 16
    _description: str = " The old double\n whammie!"
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _attack: int = 40
    _variance: int = 4
    _price: int = 72
    _inflict_type = None
    _half_time_window_begins = UInt8(2)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(22)


__all__ = ["WhompGloveItem"]
