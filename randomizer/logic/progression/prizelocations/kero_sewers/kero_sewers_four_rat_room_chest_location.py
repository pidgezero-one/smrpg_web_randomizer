from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_sewer, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeroSewersFourRatRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KeroSewersStarPrize
    _rooms = [R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_CHEST
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 42),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_3"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS,
            ["next"],
            identifier="sewers_closed_check_3",
        ),
        Jmp(["kero_sewers_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Shuffle EXP stars\" is turned off."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)


__all__ = ["KeroSewersFourRatRoomChestLocation"]
