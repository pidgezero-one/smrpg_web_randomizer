# pylint: disable=C0301

"""E0207_UNLOCK_KEEP_IF_GATED_BY_STAR_PIECES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(KEEP_GATED_BY_STAR_PIECES, ["EVENT_207_ret"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 6, ["EVENT_207_remove_map_connector"]),
        JmpToEvent(
            E3093_OPEN_ABYSS_IF_STAR_PIECE_THRESHOLD_MET, identifier="EVENT_207_ret"
        ),
        ClearBit(
            MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL,
            identifier="EVENT_207_remove_map_connector",
        ),
        SetBit(MAP_VISTA_HILL),
        RunDialog(
            dialog_id=DI2264_KEEP_OPEN,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        JmpToEvent(E3093_OPEN_ABYSS_IF_STAR_PIECE_THRESHOLD_MET),
    ]
)
