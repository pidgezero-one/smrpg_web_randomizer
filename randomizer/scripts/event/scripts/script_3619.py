# pylint: disable=C0301

"""E3619_NIMBUS_EXTERIOR_OPEN_SHOP_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_3584_ret_0"]),
        SetBit(TEMP_7043_2),
        ActionQueueAsync(
            target=MARIO, subscript=[ASPlaySound(sound=SO090_CURTAIN, channel=4)]
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 438, ["EVENT_3619_apply_tile_mod_10"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            mod_id=3),
        Return(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
            mod_id=3,
            identifier="EVENT_3619_apply_tile_mod_10"),
        Return(),
    ]
)
