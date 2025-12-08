# pylint: disable=C0301

"""E2571_BOOSTER_PASS_SECRET_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2571_pause_0"),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2571_set_bit_7"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_2571_freeze_camera_5"]),
        Jmp(["EVENT_2571_pause_0"]),
        FreezeCamera(identifier="EVENT_2571_freeze_camera_5"),
        Jmp(["EVENT_2571_pause_0"]),
        SetBit(
            DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING, identifier="EVENT_2571_set_bit_7"
        ),
        EnterArea(
            room_id=R100_BOOSTER_PASS_AREA_01,
            face_direction=SOUTHWEST,
            x=20,
            y=24,
            z=8,
            run_entrance_event=True),
        Return(),
    ]
)
