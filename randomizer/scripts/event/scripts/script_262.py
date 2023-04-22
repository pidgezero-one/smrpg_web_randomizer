# pylint: disable=C0301

"""E0262_FADE_MUSIC_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO000_SILENCE, channel=4),
        FadeOutMusicToVolume(duration=1, volume=127),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
