from randomizer.types.item import (RegularItem)
from smrpgpatchbuilder.datatypes.items.enums import (EffectType, ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class FreshenUpItem(RegularItem):
    """Freshen Up item class"""
    _item_name: str = "Freshen Up"
    _prefix = ItemPrefix.CONSUMABLE

    _text_shop_menu = "Freshen Up........"
    _remake_text_shop_menu = "PartyCleanse......"

    _item_id: int = 127
    _description: str = " Party is\n refreshed\n during battle"
    _price: int = 50
    _effect_type = EffectType.NULLIFICATION
    _inflict_type = None
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _status_immunities: list[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]

    _remake_name = "PartyCleanse"


__all__ = ["FreshenUpItem"]
