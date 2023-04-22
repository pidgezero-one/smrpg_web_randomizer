# pylint: disable=C0301

"""E0171_MIMIC_3_GRANT_STAR_PIECE_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(GAME_OVER, ["EVENT_171_reset_and_choose_game_366"]),
        JmpIfBitSet(MIMIC_3_STAR_PIECE, ["EVENT_171_ret"]),
        SetBit(MIMIC_3_STAR_PIECE),
        SetVarToConst(PRIMARY_TEMP_7000, 514),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        ResetAndChooseGame(identifier="EVENT_171_reset_and_choose_game_366"),
        Return(identifier="EVENT_171_ret"),
    ]
)
