# pylint: disable=C0301

"""E0941_KEEP_FIRST_BOSS_SET_SCRIPT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetAsyncActionScript(NPC_0, A1004_KEEP_1ST_BOSS_SUMMON_ANIMATION),
        Pause(60),
        Return(),
    ]
)
