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
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class QuartzCharmItem(Accessory):
    """Quartz Charm item class"""
    _item_name: str = "Quartz Charm"
    _prefix = ItemPrefix.RING

    _item_id: int = 94
    _description: str = " Shining source\n of power!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _price: int = 7
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _prevent_ko: bool = True
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK, TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]


__all__ = ["QuartzCharmItem"]
