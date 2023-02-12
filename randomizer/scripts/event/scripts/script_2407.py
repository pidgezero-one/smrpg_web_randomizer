# E2407_STAR_HILL_FINAL_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2407_freeze_camera_29"]),
        Return(),
        FreezeCamera(identifier="EVENT_2407_freeze_camera_29"),
        ActionQueueAsync(
            target=MARIO, subscript=[ASWalk1StepNortheast(), ASVisibilityOff()]
        ),
        Pause(32),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=13
        ),
        PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
        UnfreezeCamera(),
        Pause(32),
        FadeOutToBlack(sync=False, duration=16),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        ExitToWorldMap(area=OW31_STAR_HILL, bit_6=True, bit_7=True),
    ]
)
