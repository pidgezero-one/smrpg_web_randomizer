from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_pipe_vault, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class PipeVaultSlidingCoinRoomMiddleChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 93),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["next"]
        ),
        Jmp(["pipe_vault_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)


__all__ = ["PipeVaultSlidingCoinRoomMiddleChestLocation"]
