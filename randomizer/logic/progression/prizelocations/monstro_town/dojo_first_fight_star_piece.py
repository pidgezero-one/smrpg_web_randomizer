from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_monstro_town, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.logic.progression.prizelocations.monstro_town.dojo_first_fight import (DojoFirstFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class DojoFirstFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_1
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _parent = DojoFirstFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 290),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]
    # Flag as checked: DOJO_BOSS_1_DEFEATED

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_monstro_town(
            world, inventory
        ) and is_midgame(world, inventory)


__all__ = ["DojoFirstFightStarPiece"]
