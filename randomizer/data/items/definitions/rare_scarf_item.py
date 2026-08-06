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


class RareScarfItem(Accessory):
    """Rare Scarf item class"""
    _item_name: str = "Rare Scarf"
    _prefix = ItemPrefix.RING

    _item_id: int = 82
    _description: str = " Raises defense\n power!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _defense: int = 15
    _magic_defense: int = 15
    _price: int = 150
    _inflict_type = None

    _remake_name = "DefenseScarf"


__all__ = ["RareScarfItem"]
