from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class PowerBlastItem(RegularItem):
    """Power Blast item class"""
    _item_name: str = "Power Blast"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Power Blast......"
    _remake_text_shop_menu = "Party Energizer.."

    _item_id: int = 154
    _description: str = " Raises party's\n Attack Power\n in battle"
    _price: int = 5
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK]

    _remake_name = "PartyEnergzr"


__all__ = ["PowerBlastItem"]
