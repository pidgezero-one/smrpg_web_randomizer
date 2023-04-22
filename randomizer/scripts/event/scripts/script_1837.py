# pylint: disable=C0301

"""E1837_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1837_ret_7"]),
        SetBit(TEMP_7043_0),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkNorthPixels(4),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(4),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Pause(8),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(SLOW),
                ASJmp(["EVENT_1837_non_embedded_action_queue_8"]),
            ],
        ),
        Return(identifier="EVENT_1837_ret_7"),
        NonEmbeddedActionQueue(
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftZUpSteps(5),
                ASWalkSoutheastSteps(5),
                ASShiftZDownSteps(3),
                ASWalkNortheastSteps(7),
                ASWalkNorthwestSteps(2),
                ASWalk1StepNortheast(),
                ASWalk1StepNorthwest(),
                ASShiftZUpSteps(5),
                ASShiftZDownSteps(3),
                ASWalkNorthwestSteps(3),
                ASShiftZUpSteps(5),
                ASShiftZDownSteps(5),
                ASWalkSoutheastSteps(3),
                ASShiftZDownSteps(3),
                ASWalkSouthwestSteps(5),
                ASShiftZUpSteps(5),
                ASShiftZDownSteps(2),
                ASWalkSoutheastSteps(2),
                ASWalkNortheastSteps(14),
                ASWalkNorthwestSteps(4),
                ASPlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
                ASPause(30),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZDownSteps(4),
                ASWalkSouthwestSteps(17),
                ASPlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
                ASPause(60),
                ASJmp(["EVENT_1837_non_embedded_action_queue_8"]),
            ],
            identifier="EVENT_1837_non_embedded_action_queue_8",
        ),
    ]
)
