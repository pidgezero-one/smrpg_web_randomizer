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
from randomizer.logic.progression.prizelocations.access import (can_pass_obstacle_courses, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_exit_keep, can_clear_keep)
from randomizer.logic.progression.prizelocations.bowsers_keep.keep_final_boss_fight import (KeepFinalBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
from uuid import (uuid4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    _parent = KeepFinalBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 422),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_clear_keep(world, inventory)
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if self.prize is None:
            identifier = str(uuid4())
            assert self.override_id is not None
            first: list[list[UsableEventScriptCommand]] = [
                [JmpIfVarEqualsConst(PRIMARY_TEMP_7000, self.override_id, [identifier])]
            ]
            second: list[UsableEventScriptCommand] = [
                ClearBit(
                    RETURN_TO_OVERWORLD_AFTER_KEEP_STAR_PIECE, identifier=identifier
                ),
                JmpToEvent(E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT),
            ]
            return (first, second)
        else:
            return super().render(world)


__all__ = ["KeepFinalStarPiece"]
