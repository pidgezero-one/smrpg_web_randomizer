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


class TroopaPinItem(Accessory):
    """Troopa Pin item class"""
    _item_name: str = "Troopa Pin"
    _prefix = ItemPrefix.RING

    _item_id: int = 92
    _description: str = "Grants \"Troopa\"\nconfidence!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _speed: int = 20
    _price: int = 1000
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK]


__all__ = ["TroopaPinItem"]
