from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import uuid4
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_factory, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.logic.progression.prizelocations.inner_factory.inner_factory_fourth_fight import (InnerFactoryFourthFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactoryFourthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryFourthFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 438),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(INNER_FACTORY_ROOM_4_COMPLETED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )
    
    def render(
        self, world: GameWorld
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        (first, second) = super().render(world)
        if self.prize is not None and world.settings.get_flag(StarPiecesRequired).value > 0:
            first_id = second[0].identifier.label
            new_dest = str(uuid4())
            second[0].rename(new_dest)

            second = [
                RunEventAsSubroutine(E1980_SUMMON_FINAL_BOSS_BUTTON_IF_INNER_FACTORY_4_HAS_FINAL_STAR_PIECE, identifier=first_id)
            ] + second

            return (first, second)
        else:
            return super().render(world)
        return (first, second)


__all__ = ["InnerFactoryFourthFightStarPiece"]
