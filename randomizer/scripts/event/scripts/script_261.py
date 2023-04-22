# pylint: disable=C0301

"""E0261_FADE_MUSIC_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=1, volume=96, identifier="EVENT_261_1"),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
