from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_clear_nimbus_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_5, NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusLandCrocoItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = SignalRingPrize
    _rooms = [R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SIGNAL_RING
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 361),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_8"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_8"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_8"],
            identifier="nimbus_ck_dummy_8",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_land_hint_text"],
            identifier="nimbus_ck_dummy2_8",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)


__all__ = ["NimbusLandCrocoItemLocation"]
