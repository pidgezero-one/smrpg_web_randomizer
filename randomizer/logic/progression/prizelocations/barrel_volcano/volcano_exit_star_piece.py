from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.overworld_area_names import (OW50_BARREL_VOLCANO)
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_clear_volcano, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.logic.progression.prizelocations.barrel_volcano.volcano_exit_boss_fight import (VolcanoExitBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
from uuid import (uuid4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class VolcanoExitStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece6
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _parent = VolcanoExitBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 376),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitSet(VOLCANO_LIBERATED, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_volcano(
            world, inventory
        )

    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        if self.prize is None:
            identifier = str(uuid4())
            return (
                [
                    [
                        JmpIfVarEqualsConst(
                            PRIMARY_TEMP_7000,
                            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                            [identifier],
                        )
                    ]
                ],
                [
                    ExitToWorldMap(
                        area=OW50_BARREL_VOLCANO,
                        bit_6=True,
                        bit_7=True,
                        identifier=identifier,
                    ),
                    Return(),
                ],
            )
        else:
            return super().render(world)


__all__ = ["VolcanoExitStarPiece"]
