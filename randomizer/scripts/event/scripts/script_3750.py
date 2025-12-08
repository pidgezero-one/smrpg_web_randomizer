# pylint: disable=C0301

"""E3750_NIMBUS_MEZZANINE_FALL_TO_HOT_SPRINGS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_704A_2),
        EnterArea(
            room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS,
            face_direction=SOUTH,
            x=17,
            y=54,
            z=0,
            run_entrance_event=True),
        RunEventAsSubroutine(E0282_UNKNOWN_PIPE_VAULT),
        Return(),
    ]
)
