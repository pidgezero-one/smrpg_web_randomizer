from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_clear_ship)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerShipBeforeBossChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BANDANA_REDS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 243),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_4,
            R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            ["next"],
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def render(self, world: GameWorld) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        if self.prize is None and not world.settings.isflag_enabled(AnnoyingChests):
            world.event_scripts.delete_command_by_identifier("floating_chest_in_sunken_ship")
        return op


__all__ = ["InnerShipBeforeBossChestLocation"]
