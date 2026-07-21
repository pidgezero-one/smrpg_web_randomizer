from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_pass_obstacle_courses, not_earlygame)
from randomizer.progression.prizelocations.bowsers_keep.keep_chandelier_boss_fight import (KeepChandelierBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
from uuid import (uuid4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepChandelierStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    _parent = KeepChandelierBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 421),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfBitSet(KEEP_BOSS_2_DEFEATED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
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
                    DO_SECOND_KEEP_BOSS_FIGHT_FROM_STAR_PIECE, identifier=identifier
                ),
                JmpToEvent(E2226_KEEP_3RD_BOSS),
            ]
            return (first, second)
        else:
            return super().render(world)


__all__ = ["KeepChandelierStarPiece"]
