from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class FingerShotItem(Weapon):
    """Finger Shot item class"""
    _item_name: str = "Finger Shot"
    _prefix = ItemPrefix.GUN

    _item_id: int = 9
    _description: str = " Fingers shoot\n bullets"
    _equip_chars: list[PartyCharacter] = [GENO]
    _attack: int = 12
    _variance: int = 3
    _price: int = 50
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(16)
    _perfect_window_ends = UInt8(22)
    _half_time_window_ends = UInt8(26)


__all__ = ["FingerShotItem"]
