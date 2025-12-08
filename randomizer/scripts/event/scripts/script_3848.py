# pylint: disable=C0301

"""E3848_WORLD_MAP_PIPE_VAULT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfVarNotEqualsConst(
            LAST_OVERWORLD_MARKER_ID, 18, ["EVENT_3848_enter_area_3"]
        ),
        EnterArea(
            room_id=R055_PIPE_VAULT_ENTRANCE,
            face_direction=NORTHWEST,
            x=20,
            y=30,
            z=0,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R055_PIPE_VAULT_ENTRANCE,
            face_direction=SOUTHEAST,
            x=12,
            y=14,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3848_enter_area_3"),
        Return(),
    ]
)
