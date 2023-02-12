# E2541_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        FreezeCamera(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZUpSteps(11),
                ASSetWalkingSpeed(NORMAL),
                ASFloatingOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftNorthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftSouthwestPixels(6),
                ASSetWalkingSpeed(SLOW),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftSoutheastPixels(3),
                ASShiftSouthwestPixels(4),
                ASSetWalkingSpeed(SLOW),
            ],
        ),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftNorthwestPixels(8),
                ASShiftNortheastPixels(6),
            ],
        ),
        SetSyncActionScript(NPC_1, A0405_FOREST_MAZE_AREA_FREEMOVING_AMANITA),
        SetSyncActionScript(NPC_2, A0846_VALLEY_TOP_PIPE_RIGHT_GECKO),
        SetSyncActionScript(NPC_3, A0847_VALLEY_TOP_PIPE_MID_GECKO),
        SetSyncActionScript(NPC_5, A0194_BEAN_VALLEY_CHOMP),
        FadeInFromBlack(sync=False),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO,
            ["EVENT_2541_action_queue_async_14"],
        ),
        RunBackgroundEvent(
            event_id=E2802_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER,
            return_on_level_exit=True,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_2541_action_queue_async_14_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2541_action_queue_async_14_SUBSCRIPT_pause_1"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
            identifier="EVENT_2541_action_queue_async_14",
        ),
        UnfreezeCamera(),
        Return(),
    ]
)
