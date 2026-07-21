from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_pipe_vault)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class PipeVaultGoombaThumpinSecondPrizeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 102),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitSet(GOOMBA_THUMPIN_PRIZE_2_GRANTED, ["next"]),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)


__all__ = ["PipeVaultGoombaThumpinSecondPrizeLocation"]
