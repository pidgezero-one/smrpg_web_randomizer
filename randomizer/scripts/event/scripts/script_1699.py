# pylint: disable=C0301

"""E1699_BANDITS_WAY_4_LOADER_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_1699_pause_0"),
        JmpIfMarioInAir(["EVENT_1699_pause_action_script_3"]),
        Jmp(["EVENT_1699_pause_0"]),
        PauseActionScript(MEM_70AA, identifier="EVENT_1699_pause_action_script_3"),
        Pause(1, identifier="EVENT_1699_pause_4"),
        JmpIfMarioInAir(["EVENT_1699_pause_4"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 576),
        JmpIfComparisonResultIsLesser(["EVENT_1699_pause_0"]),
        ResumeActionScript(MEM_70AA),
        Jmp(["EVENT_1699_pause_0"]),
    ]
)
