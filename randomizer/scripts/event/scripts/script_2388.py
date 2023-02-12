# E2388_ABYSS_AMEBOID_BUTTON

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        JmpIfBitSet(ABYSS_GREEN_BUTTON, ["EVENT_2304_ret_0"]),
        SetBit(ABYSS_GREEN_BUTTON),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
        Pause(1),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=1,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=2,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=3,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=4,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=5,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=6,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=7,
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=8,
        ),
        Pause(1),
        SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
            mod_id=1,
        ),
        Return(),
    ]
)
