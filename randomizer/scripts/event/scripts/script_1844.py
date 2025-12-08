# pylint: disable=C0301

"""E1844_SUMMON_CLOUD_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 10),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1844_pause_3"]),
        Return(),
        Pause(1, identifier="EVENT_1844_pause_3"),
        JmpIfMarioInAir(["EVENT_1844_pause_3"]),
        Set70107015ToObjectXYZ(MARIO),
        AddConstToVar(Z_COORD_1, 1024),
        SetVarToConst(TEMP_7034, 52428),
        CreatePacketAt7010WithEvent(
            packet=P032_BLUE_CLOUD,
            event_id=E1845_CLOUD_BOSS,
            destinations=["EVENT_1844_pause_3"]),
        PlaySound(sound=SO044_GHOST_FLOAT, channel=6),
        Return(),
    ]
)
