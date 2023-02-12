# E2065_DOJO_LOADER_FIRST_TIME_ANIMATION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2065_pause_0"),
        Pause(1),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFaceSouthwest(),
                ASPause(30),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASPause(15),
                ASResetProperties(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetWalkingSpeed(NORMAL),
                ASShiftSouthwestSteps(2),
                ASResetProperties(),
                ASFixedFCoordOff(),
            ],
        ),
        SetBit(INITIAL_DOJO_CUTSCENE_COMPLETED),
        Return(),
    ]
)
