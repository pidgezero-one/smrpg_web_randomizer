from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class HurlyGlovesItem(Weapon):
    """Hurly Gloves item class"""
    _item_name: str = "Hurly Gloves"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 20
    _description: str = " A classic\n Mario-toss\n attack"
    _equip_chars: list[PartyCharacter] = [BOWSER]
    _attack: int = 20
    _variance: int = 5
    _price: int = 92
    _inflict_type = None
    _half_time_window_begins = UInt8(12)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(36)


__all__ = ["HurlyGlovesItem"]
