from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_factory, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_defeat_factory_bosses)
from randomizer.logic.progression.prizelocations.inner_factory.inner_factory_third_fight import (InnerFactoryThirdFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactoryThirdFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryThirdFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 437),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectNotInSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_defeat_factory_bosses(world, inventory)
        )


__all__ = ["InnerFactoryThirdFightStarPiece"]
