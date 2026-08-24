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
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BanditsWayPlatformsLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = BanditsWayStarPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_CHEST
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 34),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R078_BANDITS_WAY_AREA_04, ["next"]
        ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Shuffle EXP stars\" is turned off."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if not isinstance(self.prize, EXPStarPrize):
            world.event_scripts.get_script_by_id(
                E1538_BANDITS_WAY_STAR_CHEST_CAMERA_AND_DOGS
            ).insert_before_nth_command(0, Jmp(["EVENT_1538_jmp_to_event_2"]))
        return super().render(world)


__all__ = ["BanditsWayPlatformsLeftChestLocation"]
