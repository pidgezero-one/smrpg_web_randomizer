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


class WakeUpPinItem(Accessory):
    """Wake Up Pin item class"""
    _item_name: str = "Wake Up Pin"
    _prefix = ItemPrefix.RING

    _item_id: int = 85
    _description: str = "Prevents Mute &\nSleep attacks"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _defense: int = 3
    _magic_defense: int = 3
    _price: int = 42
    _effect_type = EffectType.PROTECTION
    _inflict_type = None
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP]


__all__ = ["WakeUpPinItem"]
