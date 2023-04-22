# pylint: disable=C0301

"""E1815_TROOPA_CLIFF_TIMER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_1815_pause_0"),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 65535, ["EVENT_1815_inc_short_3"]),
        Inc(SECONDARY_TEMP_7024),
        Inc(TEMP_7026, identifier="EVENT_1815_inc_short_3"),
        JmpIfVarNotEqualsConst(
            TEMP_7026, 10, ["EVENT_1815_set_7000_to_object_coord_7"]
        ),
        PlaySound(sound=SO147_CLICK, channel=4),
        SetVarToConst(TEMP_7026, 0),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Z,
            pixel=True,
            identifier="EVENT_1815_set_7000_to_object_coord_7",
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_1815_fade_out_music_to_volume_13"]
        ),
        JmpIfBitClear(TEMP_7044_1, ["EVENT_1815_pause_0"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 1536),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1815_pause_0"]),
        FadeOutMusicToVolume(
            duration=2, volume=127, identifier="EVENT_1815_fade_out_music_to_volume_13"
        ),
        RunEventAtReturn(E1817_TROOPA_CLIFF_FALL),
        Return(),
    ]
)
