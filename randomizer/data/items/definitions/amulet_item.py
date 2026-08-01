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
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class AmuletItem(Accessory):
    """Amulet item class"""
    _item_name: str = "Amulet"
    _prefix = ItemPrefix.RING

    _item_id: int = 78
    _description: str = " Great item,\n bad smell!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = -5
    _attack: int = 7
    _defense: int = 7
    _magic_attack: int = 7
    _magic_defense: int = 7
    _price: int = 200
    _inflict_type = None
    _elemental_resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]

    _remake_name = "BoosterCharm"


__all__ = ["AmuletItem"]
