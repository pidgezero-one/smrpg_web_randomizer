from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_7)


class MushroomKingdomChair(NPCLocationRow1):
    _originally_held = MushroomPrize
    _rooms = [
        R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _check_npc_ids = [NPC_0, NPC_7]
    _id = ShuffleLocationSelector.PEACH_SURPRISE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 16),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]


__all__ = ["MushroomKingdomChair"]
