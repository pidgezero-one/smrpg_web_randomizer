# pylint: disable=C0301

"""E3093_OPEN_ABYSS_IF_STAR_PIECE_THRESHOLD_MET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(FACTORY_GATED_BY_STAR_PIECES, ["EVENT_3093_ret_418"]),
        JmpIfVarEqualsConst(EXP_STAR_70D5, 7, ["EVENT_3093_set_bit_399"]),
        Jmp(["EVENT_3093_star_piece"], identifier="EVENT_3093_ret_418"),
        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, identifier="EVENT_3093_set_bit_399"),
        SetBit(MAP_GATE),
        JmpIfBitClear(KEEP_BOSS_3_DEFEATED, ["EVENT_3093_star_piece"]),
        RunDialog(
            dialog_id=DI2265_GATE_OPEN,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpToEvent(
            E3400_RESTART_MUSIC_AFTER_STAR_PIECE_SEQUENCE,
            identifier="EVENT_3093_star_piece"),
    ]
)
