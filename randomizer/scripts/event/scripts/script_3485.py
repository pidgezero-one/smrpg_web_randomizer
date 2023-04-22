# pylint: disable=C0301

"""E3485_MIDAS_RIVER_BOTTOM_RIGHT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=2, volume=96),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        RunEventAtReturn(E3495_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ANIMATION_AND_EXIT),
        Return(),
    ]
)
