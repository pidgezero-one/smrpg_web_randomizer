# pylint: disable=C0301

"""E3735_NIMBUS_CASTLE_FINAL_HALLWAY_APPLY_MOD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3735_apply_tile_mod_3"]),
        JmpToEvent(E3735_NIMBUS_CASTLE_FINAL_HALLWAY_APPLY_MOD),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            mod_id=0,
            identifier="EVENT_3735_apply_tile_mod_3"),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            mod_id=0),
        Return(),
    ]
)
