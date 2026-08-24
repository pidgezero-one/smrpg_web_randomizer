from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_bandits_way, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomOccupiedOutdoorGuardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, R191_MUSHROOM_KINGDOM_OUTSIDE]
    _check_npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.INVASION_EASTERN_GUARD
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 22),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)


__all__ = ["MushroomKingdomOccupiedOutdoorGuardLocation"]
