# pylint: disable=C0301

"""E3482_MIDAS_RIVER_TOP_TUNNEL_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=2, volume=96),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        RunEventAtReturn(E3491_MIDAS_RIVER_TOP_TUNNEL_ANIMATION_AND_EXIT),
        Return(),
    ]
)
