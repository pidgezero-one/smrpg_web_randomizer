# pylint: disable=C0301

"""E0206_UNLOCK_SEA_IF_GATED_BY_STAR_PIECES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(SEA_GATED_BY_STAR_PIECES, ["EVENT_206_ret"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 4, ["EVENT_206_set_bit_399"]),
        JmpToEvent(
            E0207_UNLOCK_KEEP_IF_GATED_BY_STAR_PIECES, identifier="EVENT_206_ret"
        ),
        SetBit(MAP_SEA, identifier="EVENT_206_set_bit_399"),
        SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
        RunDialog(
            dialog_id=DI2261_SEA_OPEN,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        JmpToEvent(E0207_UNLOCK_KEEP_IF_GATED_BY_STAR_PIECES),
    ]
)
