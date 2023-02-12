# E2525_STAR_HILL_2ND_ROOM_USE_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2525_freeze_camera_2"]),
        Return(),
        FreezeCamera(identifier="EVENT_2525_freeze_camera_2"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_2525_action_queue_async_3_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2525_action_queue_async_3_SUBSCRIPT_pause_0"]
                ),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
            ],
        ),
        Pause(32),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=13
        ),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        UnfreezeCamera(),
        Pause(32),
        FadeOutToBlack(sync=False, duration=16),
        EnterArea(
            room_id=R159_STAR_HILL_AREA_04,
            face_direction=SOUTHWEST,
            x=26,
            y=110,
            z=2,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
