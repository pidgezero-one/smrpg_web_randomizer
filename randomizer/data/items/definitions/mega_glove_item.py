from randomizer.types.item import (Weapon)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.numbers.classes import (UInt8)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class MegaGloveItem(Weapon):
    """Mega Glove item class"""
    _item_name: str = "Mega Glove"
    _prefix = ItemPrefix.GLOVE

    _item_id: int = 24
    _description: str = " Packs a mega\n wallop!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _attack: int = 60
    _variance: int = 6
    _price: int = 102
    _inflict_type = None
    _half_time_window_begins = UInt8(6)
    _perfect_window_begins = UInt8(12)
    _perfect_window_ends = UInt8(18)
    _half_time_window_ends = UInt8(26)


__all__ = ["MegaGloveItem"]
