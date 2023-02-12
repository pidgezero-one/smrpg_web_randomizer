# E1836_KEEP_DONKEY_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7095_4),
        RemoveObjectFromSpecificLevel(
            NPC_2, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_6, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_7, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        ActionQueueAsync(
            target=NPC_8, subscript=[ASShiftSouthwestPixels(8), ASFaceSoutheast()]
        ),
        RunBackgroundEvent(
            event_id=E1854_KEEP_DONKEY_ROOM_BACKGROUND, return_on_level_exit=True
        ),
        JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES),
    ]
)
