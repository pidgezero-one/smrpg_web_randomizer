from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class EnergizerItem(RegularItem):
    """Energizer item class"""
    _item_name: str = "Energizer"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Energizer........"

    _item_id: int = 105
    _description: str = " Raises ally's\n battle power\n during battle"
    _price: int = 2
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK]


__all__ = ["EnergizerItem"]
