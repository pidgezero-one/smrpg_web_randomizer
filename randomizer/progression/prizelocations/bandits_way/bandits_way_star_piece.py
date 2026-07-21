from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_bandits_way)
from randomizer.progression.prizelocations.bandits_way.bandits_way_boss_fight import (BanditsWayBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BanditsWayStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_PIECE
    _world_area = WorldAreaEnum.BANDITS_WAY
    _parent = BanditsWayBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 37),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        Jmp(["bandits_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_bandits_way(
            world, inventory
        )


__all__ = ["BanditsWayStarPiece"]
