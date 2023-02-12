# E3358_KEEP_BALL_SOLITAIRE_LOADER

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
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        SetBit(TEMP_7044_7),
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
