from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (YOSHI_ITEM_GRANTED)
from randomizer.logic.progression.prizelocations.access import (can_access_pipe_vault)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow5, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class YosterRaceCookieYoshiLocation(KeyItemLocation, NPCLocationRow5):
    _bias = True
    _originally_held = CookiesPrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_COOKIE
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 106),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitSet(YOSHI_ITEM_GRANTED, ["next"]),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)


__all__ = ["YosterRaceCookieYoshiLocation"]
