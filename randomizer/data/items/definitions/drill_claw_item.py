from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class DrillClawItem(Weapon):
    """Drill Claw item class"""
    _item_name: str = "Drill Claw"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 30
    _description: str = " A drilling\n claw!"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _attack: int = 40
    _variance: int = 7
    _price: int = 118
    _inflict_type = None
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(16)
    _perfect_window_ends = UInt8(24)
    _half_time_window_ends = UInt8(36)


__all__ = ["DrillClawItem"]
