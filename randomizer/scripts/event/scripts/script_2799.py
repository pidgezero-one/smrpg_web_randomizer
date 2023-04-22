# pylint: disable=C0301

"""E2799_STAR_HILL_ENTRANCE_TO_1ST_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2799_freeze_camera_2"]),
        Return(),
        FreezeCamera(identifier="EVENT_2799_freeze_camera_2"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_2799_action_queue_async_3_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2799_action_queue_async_3_SUBSCRIPT_pause_0"]
                ),
                ASOverwriteSolidity(),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
            ],
        ),
        Pause(32),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=1
        ),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        UnfreezeCamera(),
        Pause(32),
        FadeOutToBlack(sync=False, duration=16),
        EnterArea(
            room_id=R158_STAR_HILL_AREA_02,
            face_direction=NORTHWEST,
            x=10,
            y=123,
            z=2,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
