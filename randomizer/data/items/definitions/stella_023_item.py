from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class Stella023Item(Weapon):
    """Stella 023 item class"""
    _item_name: str = "Stella 023"
    _prefix = ItemPrefix.GUN

    _item_id: int = 36
    _description: str = " A cool weapon"
    _equip_chars: list[PartyCharacter] = [GENO]
    _attack: int = 62
    _variance: int = 20
    _price: int = 2
    _inflict_type = None
    _half_time_window_begins = UInt8(6)
    _perfect_window_begins = UInt8(26)
    _perfect_window_ends = UInt8(32)
    _half_time_window_ends = UInt8(36)


__all__ = ["Stella023Item"]
