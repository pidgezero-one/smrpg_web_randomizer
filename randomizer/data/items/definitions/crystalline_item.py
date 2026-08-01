from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class CrystallineItem(RegularItem):
    """Crystalline item class"""
    _item_name: str = "Crystalline"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Crystalline......."
    _remake_text_shop_menu = "Party Bracer...."

    _item_id: int = 153
    _description: str = " Raises party's\n Defense in\n battle"
    _price: int = 5
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _temp_buffs: list[TempStatBuff] = [TempStatBuff.MAGIC_DEFENSE, TempStatBuff.DEFENSE]

    _remake_name = "Party Bracer"


__all__ = ["CrystallineItem"]
