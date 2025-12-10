# pylint: disable=C0301

"""E3092_STAR_PIECE_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_3092_pause_1"),
        JmpIfMarioInAir(["EVENT_3092_pause_1"]),
        JmpIfBitSet(STAR_PIECE_MENU_UNLOCKED, ["EVENT_3092_skip"]),
        SetBit(STAR_PIECE_MENU_UNLOCKED),
        JmpIfVarEqualsConst(
            STAR_PIECE_COUNTER, 7, ["EVENT_3092_ret_418"], identifier="EVENT_3092_skip"
        ),
        Inc(STAR_PIECE_COUNTER),
        PlayMusicAtCurrentVolume(M24_GOT_A_STAR_PIECE_PART_2),
        Db(bytearray(b"\xfd\x8e\x80\x07\x01")),
        PauseScriptUntilEffectDone(),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 7, ["EVENT_3092_run_star_piece_sequence_7"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 6, ["EVENT_3092_run_star_piece_sequence_6"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 5, ["EVENT_3092_run_star_piece_sequence_5"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 4, ["EVENT_3092_run_star_piece_sequence_4"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 3, ["EVENT_3092_run_star_piece_sequence_3"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 2, ["EVENT_3092_run_star_piece_sequence_2"]),
        JmpIfVarEqualsConst(STAR_PIECE_COUNTER, 1, ["EVENT_3092_run_star_piece_sequence_1"]),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(1, identifier="EVENT_3092_run_star_piece_sequence_1"),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(2, identifier="EVENT_3092_run_star_piece_sequence_2"),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(3, identifier="EVENT_3092_run_star_piece_sequence_3"),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(4, identifier="EVENT_3092_run_star_piece_sequence_4"),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(5, identifier="EVENT_3092_run_star_piece_sequence_5"),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(6, identifier="EVENT_3092_run_star_piece_sequence_6"),
        Jmp(["EVENT_3092_db_413"]),
        RunStarPieceSequence(7, identifier="EVENT_3092_run_star_piece_sequence_7"),
        Db(bytearray(b"\xfd\x8e\xb2\x07\x01"), identifier="EVENT_3092_db_413"),
        PauseScriptUntilEffectDone(),
        JmpToEvent(E3101_STAR_PIECE_HUNT_END_GAME),
        Return(identifier="EVENT_3092_ret_418"),
    ]
)
