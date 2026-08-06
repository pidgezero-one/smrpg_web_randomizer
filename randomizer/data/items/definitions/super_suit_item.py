from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
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


class SuperSuitItem(Armor):
    """Super Suit item class"""
    _item_name: str = "Super Suit"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 71
    _description: str = " A truly fine\n suit!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = 30
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 50
    _magic_defense: int = 50
    _price: int = 700
    _effect_type = EffectType.PROTECTION
    _inflict_type = None
    _elemental_immunities: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]


__all__ = ["SuperSuitItem"]
