# pylint: disable=C0301

"""E2798_STAR_HILL_EXIT_TO_WORLD_MAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_2798_freeze_camera_2"]),
        Return(),
        FreezeCamera(identifier="EVENT_2798_freeze_camera_2"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_2798_action_queue_async_3_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2798_action_queue_async_3_SUBSCRIPT_pause_0"]
                ),
                ASOverwriteSolidity(),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
            ]),
        Pause(32),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=3
        ),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        UnfreezeCamera(),
        Pause(32),
        FadeOutToBlack(sync=False, duration=16),
        ExitToWorldMap(area=OW31_STAR_HILL, bit_6=True, bit_7=True),
        Return(),
    ]
)
