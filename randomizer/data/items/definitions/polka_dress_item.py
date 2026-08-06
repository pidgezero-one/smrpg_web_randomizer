from randomizer.types.item import (Armor)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)


class PolkaDressItem(Armor):
    """Polka Dress item class"""
    _item_name: str = "Polka Dress"
    _prefix = ItemPrefix.SHIRT

    _item_id: int = 51
    _description: str = " A flashy dress"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 160
    _inflict_type = None

    _remake_name = "Lovely Dress"


__all__ = ["PolkaDressItem"]
