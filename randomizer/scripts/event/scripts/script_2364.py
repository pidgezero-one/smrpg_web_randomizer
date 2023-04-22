# pylint: disable=C0301

"""E2364_TOWER_TOP_FLOOR_CHEST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthPixels(8),
                ASSetWalkingSpeed(NORMAL),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthPixels(8),
                ASSetWalkingSpeed(NORMAL),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASWalkSouthPixels(8),
                ASWalkNorthwestPixels(1),
                ASWalkSouthwestPixels(3),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASWalkNorthwestPixels(1), ASWalkSouthwestPixels(3)],
        ),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_2364_fade_in_from_black_async_18"]),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2364_ret_26"]),
        RunEventAsSubroutine(E3899_BOOSTER_TOWER_STAR_PIECE_SIGNAL),
        Jmp(["EVENT_2364_ret_26"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2364_fade_in_from_black_async_18"
        ),
        Return(identifier="EVENT_2364_ret_26"),
    ]
)
