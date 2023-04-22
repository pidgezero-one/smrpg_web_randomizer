# pylint: disable=C0301

"""E1839_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1839_ret_7"]),
        SetBit(TEMP_7043_1),
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
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(SLOW),
                ASJmp(["EVENT_1839_non_embedded_action_queue_8"]),
            ],
        ),
        Return(identifier="EVENT_1839_ret_7"),
        NonEmbeddedActionQueue(
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
                ASShiftZUpSteps(2),
                ASShiftZDownSteps(4),
                ASWalkNortheastSteps(4),
                ASShiftZUpSteps(7),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownSteps(8),
                ASSetWalkingSpeed(SLOW),
                ASWalkSoutheastSteps(6),
                ASShiftZUpSteps(3),
                ASWalkSouthwestSteps(6),
                ASWalkNortheastSteps(10),
                ASShiftZUpSteps(4),
                ASShiftZDownSteps(4),
                ASWalkNorthwestSteps(2),
                ASShiftZDownSteps(4),
                ASWalkSoutheastSteps(2),
                ASShiftZUpSteps(2),
                ASPlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
                ASPause(30),
                ASSetWalkingSpeed(NORMAL),
                ASWalkNorthwestSteps(6),
                ASShiftZDownSteps(2),
                ASWalkSouthwestSteps(9),
                ASShiftZUpSteps(4),
                ASPlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
                ASPause(60),
                ASJmp(["EVENT_1839_non_embedded_action_queue_8"]),
            ],
            identifier="EVENT_1839_non_embedded_action_queue_8",
        ),
    ]
)
