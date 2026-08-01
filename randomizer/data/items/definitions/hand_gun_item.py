from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HandGunItem(Weapon):
    """Hand Gun item class"""
    _item_name: str = "Hand Gun"
    _prefix = ItemPrefix.GUN

    _item_id: int = 15
    _description: str = "It packs a kick"
    _equip_chars: list[PartyCharacter] = [GENO]
    _attack: int = 24
    _variance: int = 4
    _price: int = 75
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(34)


__all__ = ["HandGunItem"]
