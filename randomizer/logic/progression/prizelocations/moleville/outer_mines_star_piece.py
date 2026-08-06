from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_moleville_entrance)
from randomizer.logic.progression.prizelocations.moleville.outer_mines_boss_fight import (OuterMinesBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class OuterMinesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [518]
    _override_id = 518
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _parent = OuterMinesBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 120),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_moleville_entrance(
            world, inventory
        )


__all__ = ["OuterMinesStarPiece"]
