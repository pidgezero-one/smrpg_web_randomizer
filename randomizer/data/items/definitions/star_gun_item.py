from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class StarGunItem(Weapon):
    """Star Gun item class"""
    _item_name: str = "Star Gun"
    _prefix = ItemPrefix.GUN

    _item_id: int = 31
    _description: str = " Try shooting\n stars!"
    _equip_chars: list[PartyCharacter] = [GENO]
    _attack: int = 57
    _variance: int = 7
    _price: int = 120
    _inflict_type = None
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(34)


__all__ = ["StarGunItem"]
