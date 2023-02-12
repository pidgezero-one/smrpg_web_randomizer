# E2353_TOWER_HENCHMAN_3

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(object=NPC_8, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_2353_stop_all_background_events_4"]
        ),
        RunDialog(
            dialog_id=DI3072_TOWER_HENCHMAN_3_WINDOW,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        StopAllBackgroundEvents(identifier="EVENT_2353_stop_all_background_events_4"),
        RunDialog(
            dialog_id=DI3073_TOWER_HENCHMAN_3,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        JmpIfBitClear(GAME_OVER, ["EVENT_2353_remove_from_current_level_9"]),
        ResetAndChooseGame(),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_2353_remove_from_current_level_9"
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromSpecificLevel(
            NPC_8, R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS
        ),
        Pause(2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
