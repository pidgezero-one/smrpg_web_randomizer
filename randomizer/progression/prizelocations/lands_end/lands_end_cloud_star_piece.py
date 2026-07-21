from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (not_earlygame)
from randomizer.progression.prizelocations.lands_end.lands_end_cloud_boss import (LandsEndCloudBoss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndCloudStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.LANDS_END_STAR_PIECE_1
    _world_area = WorldAreaEnum.LANDS_END
    _rooms = [519]
    _override_id = 519
    _parent = LandsEndCloudBoss
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 259),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        # can appear in first room
        JmpIfBitSet(LANDS_END_CLOUD_STAR_PIECE, ["next"]),
        Jmp(["mokura_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and not_earlygame(world, inventory)


__all__ = ["LandsEndCloudStarPiece"]
