from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class FrightBombItem(RegularItem):
    """Fright Bomb item class"""
    _item_name: str = "Fright Bomb"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Fright Bomb......"

    _item_id: int = 144
    _description: str = " Fear Attack on\n all enemies"
    _inflict: int = 100
    _price: int = 100
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _usable_battle: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.FEAR]


__all__ = ["FrightBombItem"]
