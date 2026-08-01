from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class SlapGloveItem(Weapon):
    """Slap Glove item class"""
    _item_name: str = "Slap Glove"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 17
    _description: str = " It slaps 'em\n silly"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _attack: int = 40
    _variance: int = 4
    _price: int = 100
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(36)


__all__ = ["SlapGloveItem"]
