# pylint: disable=C0301

"""E1706_BANDITS_WAY_LEFT_CHEST_STAR_CHECK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(20),
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1706_pause_3"]),
        Return(),
        Pause(1, identifier="EVENT_1706_pause_3"),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_1706_pause_16"]),
        SetVarToConst(TEMP_70AB, 22),
        StartLoopNTimes(3),
        JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1706_pause_9"]),
        Jmp(["EVENT_1706_inc_12"]),
        Pause(1, identifier="EVENT_1706_pause_9"),
        SummonObjectToSpecificLevel(MEM_70AB, R078_BANDITS_WAY_AREA_04),
        SetSyncActionScript(MEM_70AB, A0471_BANDITS_WAY_2_CHEST_ROOM_CHEST),
        Inc(TEMP_70AB, identifier="EVENT_1706_inc_12"),
        EndLoop(),
        Pause(3),
        Jmp(["EVENT_1706_pause_3"]),
        Pause(1, identifier="EVENT_1706_pause_16"),
        SetVarToConst(TEMP_70AB, 22),
        StartLoopNTimes(3),
        JmpIfObjectNotInSpecificLevel(
            MEM_70AB, R078_BANDITS_WAY_AREA_04, ["EVENT_1706_inc_23"]
        ),
        PauseActionScript(MEM_70AB),
        ResetCoords(MEM_70AB),
        SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
        Inc(TEMP_70AB, identifier="EVENT_1706_inc_23"),
        EndLoop(),
        Return(),
    ]
)
