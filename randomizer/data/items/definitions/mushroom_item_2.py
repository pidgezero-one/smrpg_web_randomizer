from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (
    EffectType,
    InflictFunction,
    ItemPrefix,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class MushroomItem2(RegularItem):
    """Mushroom item class"""
    _item_name: str = "Mushroom"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Mushroom........"

    _item_id: int = 175
    _description: str = " Recovers 30 HP,\n but..."
    _inflict: int = 30
    _price: int = 4
    _effect_type = EffectType.INFLICTION
    _inflict_type = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _overworld_menu_fill_fp: bool = True
    _can_target_others: bool = True
    _can_target_self: bool = False
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.MUSHROOM]


__all__ = ["MushroomItem2"]
