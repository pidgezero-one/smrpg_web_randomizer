from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class ArmorItem(Weapon):
    """Armor item class"""
    _item_name: str = "Armor"
    _prefix = ItemPrefix.EMPTY_SPACE

    _item_id: int = 1
    _description: str = ""
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _price: int = 0
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(36)


__all__ = ["ArmorItem"]
