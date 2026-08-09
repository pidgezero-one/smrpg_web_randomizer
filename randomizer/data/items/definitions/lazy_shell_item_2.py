from randomizer.types.item import (Armor)
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
from smrpgpatchbuilder.datatypes.spells.enums import (Element, Status)


class LazyShellItem2(Armor):
    """Lazy Shell item class"""
    _item_name: str = "Lazy Shell"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 72
    _description: str = " A stout and\n durable shell."
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = -50
    _attack: int = -50
    _defense: int = 127
    _magic_attack: int = -50
    _magic_defense: int = 127
    _price: int = 222
    _inflict_type = None
    _elemental_immunities: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]


__all__ = ["LazyShellItem2"]
