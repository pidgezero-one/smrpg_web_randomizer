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
from randomizer.logic.progression.prizelocations.access import (can_access_inner_nimbus, can_enter_statue_game, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusCastleStatueGamePrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FeatherPrize
    _rooms = [
        R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
        R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
    ]
    _override_id = 520
    _id = ShuffleLocationSelector.DODO_REWARD
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 343),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["next"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]
    _access_conditions = "You will always get this regardless of if you win or fail."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_enter_statue_game(world, inventory)


__all__ = ["NimbusCastleStatueGamePrizeLocation"]
