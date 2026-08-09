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
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_PlaySound)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepAfterObstaclesBossChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = InfiniteCoinsPrize
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MAGIKOOPA
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 420),
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
            NPC_0, R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, ["next"]
        ),
        Jmp(["bowsers_keep_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Shuffle Magikoopa's coin chest\" is turned off."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)

        if not isinstance(self.prize, self._originally_held):
            # only colour the chest gold if it's vanilla
            world.event_scripts.delete_command_by_identifier(
                "infinite_coin_chest_palette"
            )
            world.event_scripts.delete_command_by_identifier(
                "infinite_coin_chest_palette_2"
            )
            # give it a random sound effect
            world.event_scripts.get_subscript_command_by_identifier(
                "infinite_coin_chest_aq", "infinite_coin_chest_sfx", A_PlaySound
            ).set_sound(random.randint(1, 162))
        return op


__all__ = ["KeepAfterObstaclesBossChestLocation"]
