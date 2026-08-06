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


class FearlessPinItem(Accessory):
    """Fearless Pin item class"""
    _item_name: str = "Fearless Pin"
    _prefix = ItemPrefix.RING

    _item_id: int = 86
    _description: str = " Prevents Fear\n attacks"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 130
    _effect_type = EffectType.PROTECTION
    _inflict_type = None
    _status_immunities: list[Status] = [Status.FEAR]


__all__ = ["FearlessPinItem"]
