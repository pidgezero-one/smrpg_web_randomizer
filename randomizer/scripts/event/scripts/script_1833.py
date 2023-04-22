# pylint: disable=C0301

"""E1833_KEEP_LINEAR_PLATFORM_ROOM_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_1833_pause_0"),
        JmpIfMarioInAir(["EVENT_1833_freeze_all_npcs_until_return_3"]),
        Jmp(["EVENT_1833_pause_0"]),
        FreezeAllNPCsUntilReturn(
            identifier="EVENT_1833_freeze_all_npcs_until_return_3"
        ),
        Pause(1),
        JmpIfMarioInAir(["EVENT_1833_freeze_all_npcs_until_return_3"]),
        JmpIfBitSet(UNKNOWN_704D_1, ["EVENT_1833_freeze_all_npcs_until_return_3"]),
        UnfreezeAllNPCs(),
        Jmp(["EVENT_1833_pause_0"]),
    ]
)
