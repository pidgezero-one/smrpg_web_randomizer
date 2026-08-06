from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_pass_obstacle_courses, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepDoorRewardChest2Location(TreasureChestLocationRow2):
    _bias = True
    _originally_held = SuperSlapPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, FirstMimicFightLauncher, SecondMimicFightLauncher, InfiniteCoinsPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 414),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfBitSet(BK_OBSTACLE_2_PRIZE_RETRIEVED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(BowserDoorShuffle)
            else True
        )
        return can_pass_obstacle_courses(world, inventory) and boss_condition
    
    def render(self, world: GameWorld) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        if self.prize is None and not world.settings.isflag_enabled(AnnoyingChests):
            world.event_2496_startup += [SetBit(BK_OBSTACLE_2_PRIZE_RETRIEVED)]
        return op


__all__ = ["KeepDoorRewardChest2Location"]
