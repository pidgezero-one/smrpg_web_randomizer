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
from randomizer.logic.progression.prizelocations.access import (can_access_nimbus_castle)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusCastleOuterPrisonCellarRightNPCLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 345),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(BLUE_CELLAR_GUARD_ITEM_GRANTED, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)


__all__ = ["NimbusCastleOuterPrisonCellarRightNPCLocation"]
