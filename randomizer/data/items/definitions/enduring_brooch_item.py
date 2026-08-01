from randomizer.types.item import (Accessory)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
    GENO,
    MALLOW,
    MARIO,
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class EnduringBroochItem(Accessory):
    """Enduring Brooch item class"""
    _item_name: str = "EnduringBrch"
    _prefix = ItemPrefix.RING

    _item_id: int = 73
    _description: str = " Prevents KOs"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _price: int = 2
    _inflict_type = None
    _prevent_ko: bool = True


__all__ = ["EnduringBroochItem"]
