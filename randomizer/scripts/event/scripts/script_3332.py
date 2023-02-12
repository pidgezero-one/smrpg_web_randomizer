# E3332_VOLCANO_1ST_BOSS_PATH_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromSpecificLevel(NPC_1, R357_VOLCANO_POSTCD_AREA_01),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_3332_ret_158"]),
        PlayMusicAtDefaultVolume(M63_AXEM_RANGERS_DROP_IN),
        Return(identifier="EVENT_3332_ret_158"),
    ]
)
