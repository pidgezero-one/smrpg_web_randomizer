# pylint: disable=C0301

"""E0482_YOSTER_ISLE_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ExitToWorldMap(area=OW52_YOSTER_ISLE, bit_6=True, bit_7=True),
        Return(),
        EnterArea(
            room_id=R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT,
            face_direction=NORTHEAST,
            x=2,
            y=24,
            z=0),
        FadeInFromBlack(sync=False),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
