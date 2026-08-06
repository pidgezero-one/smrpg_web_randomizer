from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class AbleJuiceItem(RegularItem):
    """Able Juice item class"""
    _item_name: str = "Able Juice"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Able Juice........"
    _remake_text_shop_menu = "CleanseJuice...."

    _item_id: int = 103
    _description: str = " Heals status\n problems\n during battle"
    _price: int = 4
    _effect_type = EffectType.NULLIFICATION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]

    _remake_name = "CleanseJuice"


__all__ = ["AbleJuiceItem"]
