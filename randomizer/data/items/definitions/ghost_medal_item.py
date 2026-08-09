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
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class GhostMedalItem(Accessory):
    """Ghost Medal item class"""
    _item_name: str = "Ghost Medal"
    _prefix = ItemPrefix.RING

    _item_id: int = 89
    _description: str = "Raises defense\nwhile attacking"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _price: int = 1600
    _inflict_type = None
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]


__all__ = ["GhostMedalItem"]
