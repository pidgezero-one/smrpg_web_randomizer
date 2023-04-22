# pylint: disable=C0301

"""E3079_EXP_STAR_LEVELUP_SCREEN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToMainThread(),
        ClearBit(TEMP_7076_0),
        SetBit(EXP_STAR_BIT_5),
        Set01D8Bit3(),
        JmpIfBitClear(UNKNOWN_7064_5, ["EVENT_3079_enable_controls_7"]),
        RunLevelupBonusSequence(),
        FadeInFromBlack(sync=False),
        EnableControls(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_3079_enable_controls_7",
        ),
        JmpIfBitClear(DODO_PRESENT_IN_NIMBUS_HALL, ["EVENT_3079_music"]),
        ClearBit(DODO_PRESENT_IN_NIMBUS_HALL),
        JmpIfBitClear(ALTERNATE_STAR_PIECE_WIN_CONDITION, ["EVENT_3079_music"]),
        JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_3079_music"]),
        SetBit(STATUE_KEEPER_STAR_PIECE),
        SetVarToConst(PRIMARY_TEMP_7000, 520),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        JmpToEvent(
            E3400_RESTART_MUSIC_AFTER_STAR_PIECE_SEQUENCE, identifier="EVENT_3079_music"
        ),
        Return(),
    ]
)
