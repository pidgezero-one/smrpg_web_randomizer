# pylint: disable=C0301

"""E2575_TOWER_8BIT_MUSIC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TOWER_8BIT_EASTER_EGG_BIT_1, ["EVENT_2575_ret_8"]),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        PlayMusicAtDefaultVolume(M30_LONG_LONG_AGO),
        Return(identifier="EVENT_2575_ret_8"),
    ]
)
