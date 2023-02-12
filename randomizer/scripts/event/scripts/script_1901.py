# E1901_ABYSS_AXEM_PIT_PLATFORMS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1901_ret_6"]),
        SetBit(TEMP_7043_0),
        RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
        ActionQueueSync(target=MARIO, subscript=[ASShadowOff()]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(SLOW),
                ASShiftNortheastSteps(4),
                ASWalk1StepNorthwest(),
                ASShiftSouthwestSteps(4),
                ASWalk1StepSoutheast(),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthwestSteps(4),
                ASWalk1StepSoutheast(),
                ASShiftNortheastSteps(4),
                ASWalk1StepNorthwest(),
                ASFaceSouthwest(),
                ASPause(1),
                ASClearBit(TEMP_7043_0),
            ],
        ),
        Return(identifier="EVENT_1901_ret_6"),
    ]
)
