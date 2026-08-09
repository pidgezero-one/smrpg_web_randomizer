from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_access_chapel_postgame_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow4, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreBossFightRemakeItemDrop(NPCLocationRow4):
    _bias = True
    _originally_held = EnduringBroochPrize
    _rooms = [R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_ITEM_DROP
    _world_area = WorldAreaEnum.MARRYMORE
    _remake_only = True
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 203),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(POSTGAME_CHAPEL_COMPLETE, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["marrymore_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]
    _access_conditions = "Must first defeat the boss fight at Marrymore and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel_postgame_boss(world, inventory)


__all__ = ["MarrymoreBossFightRemakeItemDrop"]
