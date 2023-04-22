# pylint: disable=C0301

"""E0729_SEVERAL_MARRYMORE_ROOM_LOADERS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 153, ["EVENT_729_apply_tile_mod_21"]),
        ApplySolidityModToLevel(
            permanent=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=1
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=0
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
            mod_id=0,
            identifier="EVENT_729_apply_tile_mod_21",
        ),
        JmpToEvent(E0641_MARRYMORE_ANTECHAMBER_LOADER_EXTENSION),
    ]
)
