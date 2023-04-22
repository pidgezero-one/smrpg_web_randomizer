# pylint: disable=C0301

"""E1612_SUMMON_GECKITS_IN_CANNON_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_9),
        RemoveObjectFromCurrentLevel(NPC_10),
        RemoveObjectFromCurrentLevel(NPC_11),
        RemoveObjectFromCurrentLevel(NPC_12),
        Pause(21),
        SetVarToConst(TEMP_70AB, 25),
        StartLoopNTimes(3),
        JmpIfObjectNotInSpecificLevel(
            MEM_70AB,
            R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
            ["EVENT_1612_inc_13"],
        ),
        SetSyncActionScript(MEM_70AB, A0126_CANNON_GECKIT),
        Inc(TEMP_70AB, identifier="EVENT_1612_inc_13"),
        EndLoop(),
        Pause(238),
        SetVarToConst(TEMP_70AB, 29),
        StartLoopNTimes(3),
        JmpIfObjectNotInSpecificLevel(
            MEM_70AB,
            R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
            ["EVENT_1612_inc_20"],
        ),
        SetSyncActionScript(MEM_70AB, A0126_CANNON_GECKIT),
        Inc(TEMP_70AB, identifier="EVENT_1612_inc_20"),
        EndLoop(),
        Return(),
    ]
)
