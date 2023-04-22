# pylint: disable=C0301

"""E1115_SUMMON_HINT_TADPOLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_6, ["EVENT_1115_ret_3"]),
        SetSyncActionScript(NPC_2, A0562_SONG_HINT_TADPOLE_SUMMONING),
        Return(identifier="EVENT_1115_ret_3"),
    ]
)
