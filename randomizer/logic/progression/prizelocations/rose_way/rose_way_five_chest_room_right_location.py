from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow3, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_2)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class RoseWayFiveChestRoomRightLocation(TreasureChestLocationRow3):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_3
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 66),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SeeYaPrize) or expect_halfway_decent_movement(world, inventory)


__all__ = ["RoseWayFiveChestRoomRightLocation"]
