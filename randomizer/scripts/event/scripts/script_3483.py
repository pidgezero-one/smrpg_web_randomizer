# pylint: disable=C0301

"""E3483_MIDAS_RIVER_MID_LEFT_OR_MID_RIGHT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=2, volume=96),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        JmpIfBitSet(
            MIDAS_RIVER_TUNNEL_2_DIRECTION, ["EVENT_3483_run_event_at_return_5"]
        ),
        RunEventAtReturn(E3492_MIDAS_RIVER_MID_LEFT_TUNNEL_ANIMATION_AND_EXIT),
        Return(),
        RunEventAtReturn(
            E3493_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT,
            identifier="EVENT_3483_run_event_at_return_5",
        ),
        Return(),
    ]
)
