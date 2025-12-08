# pylint: disable=C0301

"""E3869_WORLD_MAP_ABYSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        ClearBit(ABYSS_ENTRANCE_DIRECTIONAL_BIT),
        FadeOutMusicToVolume(duration=0, volume=0),
        EnterArea(
            room_id=R350_SMITHY_FACTORY_AREA_01,
            face_direction=NORTHEAST,
            x=4,
            y=27,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
