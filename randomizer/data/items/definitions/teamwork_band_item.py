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


class TeamworkBandItem(Accessory):
    """Teamwork Band item class"""
    _item_name: str = "TeamworkBand"
    _prefix = ItemPrefix.RING

    _item_id: int = 95
    _description: str = " It's a headband"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _price: int = 5
    _inflict_type = None
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK, TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]


__all__ = ["TeamworkBandItem"]
