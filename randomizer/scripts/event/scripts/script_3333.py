# E3333_VOLCANO_GENERIC_LOADER_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 50, identifier="EVENT_3333_set_0"),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        Set7000ToCurrentLevel(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 361, ["EVENT_3333_jmp_if_7000_equals_short_3_2"]
        ),
        ActionQueueAsync(target=NPC_1, subscript=[ASSetPriority(2), ASSetPriority(3)]),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            358,
            ["EVENT_3333_jmp_if_7000_equals_short_3"],
            identifier="EVENT_3333_jmp_if_7000_equals_short_3_2",
        ),
        ActionQueueAsync(target=NPC_2, subscript=[ASSetPriority(2), ASSetPriority(3)]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            354,
            ["EVENT_3333_run_background_event_5_"],
            identifier="EVENT_3333_jmp_if_7000_equals_short_3",
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToObjectXY(MARIO),
                ASSet700CToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
                ASFaceEast7C(),
                ASPause(1),
            ],
        ),
        RunBackgroundEvent(event_id=E3329_JUMPING_FIREBALLS, return_on_level_exit=True),
        Return(),
        RunBackgroundEvent(
            event_id=E3329_JUMPING_FIREBALLS,
            return_on_level_exit=True,
            identifier="EVENT_3333_run_background_event_5_",
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3333_ret_6_"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3333_ret_6_"]),
        RunEventAsSubroutine(E3913_VOLCANO_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3333_ret_6_"),
    ]
)
