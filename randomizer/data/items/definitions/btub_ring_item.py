from randomizer.types.item import (Accessory)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element)


class BtubRingItem(Accessory):
    """Btub Ring item class"""
    _item_name: str = "B'tub Ring"
    _prefix = ItemPrefix.RING

    _item_id: int = 83
    _description: str = "You'll win her\nheart with this!"
    _equip_chars: list[PartyCharacter] = [TOADSTOOL]
    _price: int = 145
    _inflict_type = None
    _elemental_resistances: list[Element] = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]

    _remake_name = "Nurture Ring"


__all__ = ["BtubRingItem"]
