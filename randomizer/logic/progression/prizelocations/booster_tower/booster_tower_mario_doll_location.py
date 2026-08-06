from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_do_tower_curtain_game)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerMarioDollLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = MarioDollPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MARIO_DOLL
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 167),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check___"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check___"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check___"],
            identifier="returned_mario_doll_check___",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check___"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            ["next"],
            identifier="tower_boss_2_check___",
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory)

    def grant(self, world: GameWorld | None = None) -> EventScript:
        # The shuffled prize is bonked off the curtain rod during a scripted sequence,
        # not walked onto at leisure, so its "got item" box must wait for A ([await]),
        # like the ship-puzzle/altar packets - not auto-terminate like an ordinary
        # freestanding pickup. Reuse packet_grant, whose variants are exactly the
        # [await] copies of every standing grant.
        #
        # packet_grant also strips the persistent presence write, but that write is
        # redundant here: the room-192 loader (E1359) gates NPC_5's respawn on
        # CURTAIN_MINIGAME_COMPLETED (set unconditionally on curtain-game win, E1368),
        # so NPC_5 stays gone on re-entry regardless. The variants keep the object-local
        # despawn (visibility off) that hides it for the current visit.
        if self.prize is None:
            return EventScript([Return()])
        packet_grant = self.prize.packet_grant
        if packet_grant is None:
            return EventScript([Return()])
        return packet_grant


__all__ = ["BoosterTowerMarioDollLocation"]
