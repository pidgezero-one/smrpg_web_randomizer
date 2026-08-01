from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class BadMushroomItem(RegularItem):
    """Bad Mushroom item class"""
    _item_name: str = "Bad Mushroom"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Bad Mushroom...."
    _remake_text_shop_menu = "PoisonMushroom.."

    _item_id: int = 112
    _description: str = " Poisons\n an enemy"
    _inflict: int = 50
    _price: int = 30
    _effect_type = EffectType.INFLICTION
    _inflict_type = None
    _usable_battle: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.POISON]

    _remake_name = "PoisonShroom"


__all__ = ["BadMushroomItem"]
