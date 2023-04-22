# pylint: disable=C0301

"""E0093_BACKGROUND_EVENT_FOR_SLOT_MACHINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([X, A, Y, B]),
        FreezeAllNPCsUntilReturn(),
        Pause(1, identifier="EVENT_93_pause"),
        JmpIfBitSet(TEMP_7044_2, ["EVENT_93_pause"]),
        UnfreezeAllNPCs(),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
