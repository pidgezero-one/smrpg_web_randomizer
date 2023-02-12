# E1311_TOWER_CHECKERBOARD_LOCKED_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ITEM_ID, RoomKey),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1311_apply_tile_mod_5"]),
        RunDialog(
            dialog_id=DI1941_NEED_ROOM_KEY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            mod_id=32,
            identifier="EVENT_1311_apply_tile_mod_5",
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromSpecificLevel(
            NPC_6,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
        ),
        RemoveOneOfItemFromInventory(RoomKey),
        Return(),
    ]
)
