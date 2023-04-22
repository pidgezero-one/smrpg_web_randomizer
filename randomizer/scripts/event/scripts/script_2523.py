# pylint: disable=C0301

"""E2523_STAR_HILL_1ST_ROOM_USE_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(TEMP_70AE, 5, ["EVENT_2523_freeze_camera_2"]),
        Return(),
        FreezeCamera(identifier="EVENT_2523_freeze_camera_2"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_2523_action_queue_async_3_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2523_action_queue_async_3_SUBSCRIPT_pause_0"]
                ),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
            ],
        ),
        Pause(32),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R158_STAR_HILL_AREA_02, mod_id=11
        ),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        UnfreezeCamera(),
        Pause(32),
        FadeOutToBlack(sync=False, duration=16),
        EnterArea(
            room_id=R157_STAR_HILL_AREA_03,
            face_direction=SOUTHWEST,
            x=13,
            y=24,
            z=2,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
