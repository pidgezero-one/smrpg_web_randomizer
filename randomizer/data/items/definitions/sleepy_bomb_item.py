from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class SleepyBombItem(RegularItem):
    """Sleepy Bomb item class"""
    _item_name: str = "Sleepy Bomb"
    _prefix = ItemPrefix.BOMB

    _text_shop_menu = "Sleepy Bomb......"

    _item_id: int = 111
    _description: str = " Puts enemies\n to sleep"
    _price: int = 1
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.SLEEP]


__all__ = ["SleepyBombItem"]
