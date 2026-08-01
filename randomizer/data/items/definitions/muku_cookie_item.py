from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    EffectType,
    InflictFunction,
    ItemPrefix,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class MukuCookieItem(RegularItem):
    """Muku Cookie item class"""
    _item_name: str = "Muku Cookie"
    _prefix = ItemPrefix.DOT

    _text_shop_menu = "Muku Cookie......"
    _remake_text_shop_menu = "ThrophCookie....."

    _item_id: int = 120
    _description: str = " Muku! Muku-\n muku! Muka?"
    _inflict: int = 69
    _price: int = 69
    _effect_type = EffectType.NULLIFICATION
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _overworld_menu_fill_fp: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]

    _remake_name = "ThrophCookie"


__all__ = ["MukuCookieItem"]
