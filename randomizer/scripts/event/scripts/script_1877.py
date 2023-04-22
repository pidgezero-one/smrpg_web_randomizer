# pylint: disable=C0301

"""E1877_KEEP_ROTATING_ROOM_LOADER_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_1877_pause_0"),
        JmpIfMarioInAir(["EVENT_1877_pause_action_script_3"]),
        Jmp(["EVENT_1877_pause_0"]),
        PauseActionScript(MEM_70AA, identifier="EVENT_1877_pause_action_script_3"),
        Pause(1),
        JmpIfMarioInAir(["EVENT_1877_pause_action_script_3"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 384),
        JmpIfComparisonResultIsLesser(["EVENT_1877_pause_0"]),
        ResumeActionScript(MEM_70AA),
        Jmp(["EVENT_1877_pause_0"]),
    ]
)
