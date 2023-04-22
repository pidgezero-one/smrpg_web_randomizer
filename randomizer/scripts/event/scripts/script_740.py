# pylint: disable=C0301

"""E0740_NIMBUS_LAND_OCCUPIED_CASTLE_FRONT_ENTRANCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=2, volume=0),
        Pause(4),
        EnterArea(
            room_id=R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            face_direction=NORTHEAST,
            x=1,
            y=35,
            z=0,
            run_entrance_event=True,
        ),
        PlayMusicAtDefaultVolume(M61_VALENTINA),
        Return(),
    ]
)
