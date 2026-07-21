from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_monstro_town, not_earlygame)
from randomizer.progression.prizelocations.monstro_town.dojo_fourth_fight import (DojoFourthFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class DojoFourthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_4
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 517
    _parent = DojoFourthFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 293),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )


__all__ = ["DojoFourthFightStarPiece"]
