# pylint: disable=C0301

"""E1919_ABYSS_BIG_CONVEYOR_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        PlaySound(sound=SO058_INSERT, channel=6),
        JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_1919_action_queue_async_7"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
                ASWalkNorthwestSteps(8),
            ],
        ),
        JmpToSubroutine(["EVENT_1919_enable_controls_until_return_11"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkSoutheastSteps(8),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        Return(),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSoutheastSteps(8),
            ],
            identifier="EVENT_1919_action_queue_async_7",
        ),
        JmpToSubroutine(["EVENT_1919_enable_controls_until_return_11"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkNorthwestSteps(8),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_1919_enable_controls_until_return_11",
        ),
        Pause(1, identifier="EVENT_1919_pause_12"),
        JmpIfMarioInAir(["EVENT_1919_ret_15"]),
        Jmp(["EVENT_1919_pause_12"]),
        Return(identifier="EVENT_1919_ret_15"),
    ]
)
