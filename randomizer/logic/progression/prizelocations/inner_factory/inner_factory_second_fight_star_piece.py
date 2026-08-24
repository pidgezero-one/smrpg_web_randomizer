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
from randomizer.logic.progression.prizelocations.inner_factory.inner_factory_second_fight import (InnerFactorySecondFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactorySecondFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_2
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactorySecondFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 436),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(INNER_FACTORY_ROOM_2_COMPLETED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_defeat_factory_bosses(world, inventory)
        )


__all__ = ["InnerFactorySecondFightStarPiece"]
