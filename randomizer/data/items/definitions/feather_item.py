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


class FeatherItem(Accessory):
    """Feather item class"""
    _item_name: str = "Feather"
    _prefix = ItemPrefix.RING

    _item_id: int = 91
    _description: str = " Speed up by 20"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = 20
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 666
    _inflict_type = None


__all__ = ["FeatherItem"]
