from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_pass_obstacle_courses, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_exit_keep, can_clear_keep)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepInvisibleBridgeFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrightBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    # no reloadables in bowser's keep red door rooms, too annoying for the player
    _blacklist = [EXPStarPrize, InfiniteCoinsPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 380),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_exit_keep(world, inventory) and can_exit_keep(world, inventory)


__all__ = ["KeepInvisibleBridgeFrontChestLocation"]
