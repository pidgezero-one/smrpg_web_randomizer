from randomizer.types.item import (Accessory)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class AttackScarfItem(Accessory):
    """Attack Scarf item class"""
    _item_name: str = "Attack Scarf"
    _prefix = ItemPrefix.RING

    _item_id: int = 81
    _description: str = " So comfy it'll\n make you jump!"
    _equip_chars: list[PartyCharacter] = [MARIO]
    _speed: int = 30
    _attack: int = 30
    _defense: int = 30
    _magic_attack: int = 30
    _magic_defense: int = 30
    _price: int = 1500
    _inflict_type = None
    _prevent_ko: bool = True


__all__ = ["AttackScarfItem"]
