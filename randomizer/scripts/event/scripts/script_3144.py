# E3144_ROSE_WAY_MAIN_ROOM_PLATFORMS_BACKGROUND

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=MARIO, subscript=[ASResetProperties()]),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        SetVarToConst(TEMP_70A9, 20),
        StartLoopNTimes(6),
        PauseActionScript(MEM_70A9),
        Inc(TEMP_70A9),
        EndLoop(),
        ResumeActionScript(MEM_70AA),
        RunBackgroundEvent(
            event_id=E3143_ROSE_WAY_MAIN_ROOM_PLATFORMS, return_on_level_exit=True
        ),
        Return(),
    ]
)
