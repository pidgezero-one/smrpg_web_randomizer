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
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class SafetyBadgeItem(Accessory):
    """Safety Badge item class"""
    _item_name: str = "Safety Badge"
    _prefix = ItemPrefix.RING

    _item_id: int = 75
    _description: str = "Prevents Mute &\nPoison attacks"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 500
    _inflict_type = None
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]


__all__ = ["SafetyBadgeItem"]
