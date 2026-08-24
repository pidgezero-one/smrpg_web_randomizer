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
from randomizer.logic.progression.prizelocations.access import (can_access_late_nimbus, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_10, NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusCastleBackHallwayOccupiedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = NimbusLandStarPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_CHEST
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [InfiniteCoinsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 356),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, ["next"]
        ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_4"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_4"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_4"],
            identifier="nimbus_ck_dummy_4",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_castle_hint_text"],
            identifier="nimbus_ck_dummy2_4",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_castle_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Shuffle EXP stars\" is turned off."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_late_nimbus(world, inventory)


__all__ = ["NimbusCastleBackHallwayOccupiedChestLocation"]
