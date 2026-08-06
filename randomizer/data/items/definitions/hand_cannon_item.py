from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HandCannonItem(Weapon):
    """Hand Cannon item class"""
    _item_name: str = "Hand Cannon"
    _prefix = ItemPrefix.GUN

    _item_id: int = 26
    _description: str = " Shoots bullets\n from elbow!"
    _equip_chars: list[PartyCharacter] = [GENO]
    _attack: int = 45
    _variance: int = 6
    _price: int = 105
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(46)
    _perfect_window_ends = UInt8(52)
    _half_time_window_ends = UInt8(64)


__all__ = ["HandCannonItem"]
