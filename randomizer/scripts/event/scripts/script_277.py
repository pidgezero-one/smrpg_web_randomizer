# pylint: disable=C0301

"""E0277_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7032),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_277_jmp_if_var_equals_const_4"]
        ),
        Jmp(["EVENT_277_action_queue_async_8"]),
        JmpIfVarEqualsConst(
            TEMP_7032,
            1,
            ["EVENT_277_action_queue_async_14"],
            identifier="EVENT_277_jmp_if_var_equals_const_4",
        ),
        JmpIfVarEqualsConst(TEMP_7032, 3, ["EVENT_277_action_queue_async_16"]),
        JmpIfVarEqualsConst(TEMP_7032, 5, ["EVENT_277_action_queue_async_18"]),
        JmpIfVarEqualsConst(TEMP_7032, 7, ["EVENT_277_action_queue_async_20"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xfd$\x00\x10")),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=PRIMARY_TEMP_7000),
            ],
            identifier="EVENT_277_action_queue_async_8",
        ),
        Mem7000AndConst(0x00C0),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_277_action_queue_async_14"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_277_action_queue_async_16"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_277_action_queue_async_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 192, ["EVENT_277_action_queue_async_20"]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(2),
                ASSetSpriteSequence(
                    index=6, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(5),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(5),
                ASEndLoop(),
            ],
            identifier="EVENT_277_action_queue_async_14",
        ),
        Jmp(["EVENT_277_action_queue_async_21"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(2),
                ASSetSpriteSequence(index=6, is_mold=True, looping=True),
                ASPause(5),
                ASSetSpriteSequence(index=0, is_mold=True, looping=True),
                ASPause(5),
                ASEndLoop(),
            ],
            identifier="EVENT_277_action_queue_async_16",
        ),
        Jmp(["EVENT_277_action_queue_async_21"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(2),
                ASSetSpriteSequence(index=3, is_mold=True, looping=True),
                ASPause(5),
                ASSetSpriteSequence(index=7, is_mold=True, looping=True),
                ASPause(5),
                ASEndLoop(),
            ],
            identifier="EVENT_277_action_queue_async_18",
        ),
        Jmp(["EVENT_277_action_queue_async_21"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(2),
                ASSetSpriteSequence(
                    index=3, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(5),
                ASSetSpriteSequence(
                    index=7, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(5),
                ASEndLoop(),
            ],
            identifier="EVENT_277_action_queue_async_20",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASCopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
                ASFaceEast7C(),
            ],
            identifier="EVENT_277_action_queue_async_21",
        ),
        ClearBit(TEMP_7044_7),
        Return(),
    ]
)
