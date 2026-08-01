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
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class AntidotePinItem(Accessory):
    """Antidote Pin item class"""
    _item_name: str = "Antidote Pin"
    _prefix = ItemPrefix.RING

    _item_id: int = 84
    _description: str = " Prevents\n poison damage"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _defense: int = 2
    _magic_defense: int = 2
    _price: int = 28
    _effect_type = EffectType.PROTECTION
    _inflict_type = None
    _status_immunities: list[Status] = [Status.POISON]


__all__ = ["AntidotePinItem"]
