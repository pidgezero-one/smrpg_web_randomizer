# pylint: disable=C0301

"""E0267_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(GAME_OVER_COUNTER_MAYBE, 0),
        ClearBit(TEMP_7044_0),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
