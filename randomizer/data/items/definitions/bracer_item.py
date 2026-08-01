from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class BracerItem(RegularItem):
    """Bracer item class"""
    _item_name: str = "Bracer"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Bracer..........."

    _item_id: int = 104
    _description: str = " Raises ally's\n def. in battle"
    _price: int = 2
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]


__all__ = ["BracerItem"]
