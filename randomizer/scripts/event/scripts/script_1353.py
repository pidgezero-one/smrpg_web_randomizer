# pylint: disable=C0301

"""E1353_TOWER_CHECKERBOARD_ROOM_LOCKED_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(KEEP_BOSS_2_DEFEATED, ["EVENT_1353_pause_3"]),
        RunDialog(
            dialog_id=DI2801_NEED_THE_KEY,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        Pause(5, identifier="EVENT_1353_pause_3"),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            mod_id=32,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromSpecificLevel(
            NPC_4,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
        ),
        Pause(5),
        RemoveOneOfItemFromInventory(RoomKey),
        Return(),
    ]
)
