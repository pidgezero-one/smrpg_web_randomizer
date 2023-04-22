# pylint: disable=C0301

"""E3808_ENDING_CREDITS_RACE_AUDIENCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StartLoopNTimes(2),
        SetSyncActionScript(NPC_2, A0636_54_VELOCITY_SINGLE_JUMP),
        SetSyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(60),
        SetSyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
        SetSyncActionScript(NPC_1, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(60),
        EndLoop(),
        Return(),
    ]
)
