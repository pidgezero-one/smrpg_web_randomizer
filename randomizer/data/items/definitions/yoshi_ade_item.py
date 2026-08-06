from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class YoshiAdeItem(RegularItem):
    """Yoshi Ade item class"""
    _item_name: str = "Yoshi-Ade"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Yoshi-Ade........"

    _item_id: int = 106
    _description: str = " Power raised\n during battle"
    _price: int = 200
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_ATTACK, TempStatBuff.ATTACK, TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]


__all__ = ["YoshiAdeItem"]
