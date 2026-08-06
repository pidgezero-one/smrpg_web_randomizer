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
from randomizer.logic.progression.prizelocations.access import (can_clear_nimbus_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_10, NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusCastleBusinessCentreLiberatedChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 359),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerEnabledInSpecificLevel(
            NPC_0, R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, ["next"]
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_10, R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_6"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_6"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_6"],
            identifier="nimbus_ck_dummy_6",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_6",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)


__all__ = ["NimbusCastleBusinessCentreLiberatedChestLocation"]
