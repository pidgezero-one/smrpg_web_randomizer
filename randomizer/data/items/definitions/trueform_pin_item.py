from randomizer.types.item import (Accessory)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    BOWSER,
    GENO,
    MALLOW,
    MARIO,
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class TrueformPinItem(Accessory):
    """Trueform Pin item class"""
    _item_name: str = "Trueform Pin"
    _prefix = ItemPrefix.RING

    _item_id: int = 87
    _description: str = " You won't be\n turned into\n Mushrooms or\n Scarecrows!"
    _equip_chars: list[PartyCharacter] = [MARIO, TOADSTOOL, BOWSER, GENO, MALLOW]
    _defense: int = 4
    _magic_defense: int = 4
    _price: int = 60
    _inflict_type = None
    _status_immunities: list[Status] = [Status.MUSHROOM, Status.SCARECROW]


__all__ = ["TrueformPinItem"]
