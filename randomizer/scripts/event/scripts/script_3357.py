# E3357_KEEP_BUTTON_GAME_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ROSE_WAY_703E, 0),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASWalkToXYCoords(x=23, y=31), ASFaceNorthwest(), ASPause(1)],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftZUpSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
            ],
        ),
        PlayMusicAtDefaultVolume(M36_EXPLANATION),
        StartLoopNTimes(15),
        SetSyncActionScript(MEM_70A9, A0281_KEEP_TOPPER_GAME_SET_BUTTON_OR_BALL_STATE),
        Inc(TEMP_70A9),
        EndLoop(),
        Return(),
    ]
)
