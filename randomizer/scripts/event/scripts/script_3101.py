# pylint: disable=C0301

"""E3101_STAR_PIECE_HUNT_END_GAME"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(WIN_CONDITION_STAR_PIECES, ["EVENT_3101_ret_418_"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 7, ["EVENT_3101_set_bit_399"]),
        FadeInFromBlack(sync=False, identifier="EVENT_3101_ret_418_"),
        JmpToEvent(E0206_UNLOCK_SEA_IF_GATED_BY_STAR_PIECES),
        JmpToEvent(
            E3886_END_GAME_CONTAINER_FROM_ALT_WIN_CONDITIONS,
            identifier="EVENT_3101_set_bit_399",
        ),
    ]
)
