# E0377_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_REPEATING_SHYSTERS_POSITION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(NPC_2, A0108_MK_HALL_REPEATING_HENCHMEN),
        PauseActionScript(NPC_0, identifier="EVENT_377_pause_action_script_1"),
        StartAsyncEmbeddedActionScript(
            target=NPC_0, prefix=0xF1, subscript=[ASBPL262728()]
        ),
        SetSyncActionScript(NPC_0, A0110_MK_HALL_REPEATING_HENCHMEN),
        Pause(150),
        PauseActionScript(NPC_1),
        StartAsyncEmbeddedActionScript(
            target=NPC_1, prefix=0xF1, subscript=[ASBPL262728()]
        ),
        SetSyncActionScript(NPC_1, A0110_MK_HALL_REPEATING_HENCHMEN),
        Pause(150),
        Jmp(["EVENT_377_pause_action_script_1"]),
    ]
)
