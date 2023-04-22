# pylint: disable=C0301

"""E3484_MIDAS_RIVER_BOTTOM_LEFT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=2, volume=96),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        RunEventAtReturn(E3494_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_ANIMATION_AND_EXIT),
        Return(),
    ]
)
