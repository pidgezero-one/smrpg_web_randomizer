from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MALLOW,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class StickyGloveItem(Weapon):
    """Sticky Glove item class"""
    _item_name: str = "Sticky Glove"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 27
    _description: str = " Launches a\n punch attack."
    _equip_chars: list[PartyCharacter] = [MALLOW]
    _attack: int = 60
    _variance: int = 6
    _price: int = 98
    _inflict_type = None
    _half_time_window_begins = UInt8(5)
    _perfect_window_begins = UInt8(12)
    _perfect_window_ends = UInt8(18)
    _half_time_window_ends = UInt8(26)


__all__ = ["StickyGloveItem"]
