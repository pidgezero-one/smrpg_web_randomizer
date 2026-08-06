from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class RedEssenceItem(RegularItem):
    """Red Essence item class"""
    _item_name: str = "Red Essence"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Red Essence......"

    _item_id: int = 107
    _description: str = " You won't be\n attacked for\n 3 turns\n during battle"
    _price: int = 400
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.INVINCIBLE]


__all__ = ["RedEssenceItem"]
