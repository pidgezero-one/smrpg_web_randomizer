from randomizer.types.item import (Accessory)
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


class SafetyRingItem(Accessory):
    """Safety Ring item class"""
    _item_name: str = "Safety Ring"
    _prefix = ItemPrefix.RING

    _item_id: int = 77
    _description: str = " Guards against\n mortal blows."
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = 5
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 800
    _effect_type = EffectType.PROTECTION
    _inflict_type = None
    _prevent_ko: bool = True
    _elemental_immunities: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]


__all__ = ["SafetyRingItem"]
