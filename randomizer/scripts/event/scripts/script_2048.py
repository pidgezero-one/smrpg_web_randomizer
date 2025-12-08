# pylint: disable=C0301

"""E2048_MONSTRO_TOWN_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, ["EVENT_2048_set_bit_9"]),
        CopyVarToVar(from_var=MONSTRO_THWOMP_COUNTER, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2048_jmp_if_bit_set_11"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASLoadMemory(PRIMARY_TEMP_7000),
                ASWalkSouthwestPixels(2),
                ASEndLoop(),
            ]),
        Jmp(["EVENT_2048_jmp_if_bit_set_11"]),
        SetBit(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, identifier="EVENT_2048_set_bit_9"),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASTransferToXYZF(x=11, y=62, z=8, direction=EAST)]
        ),
        JmpIfBitClear(
            TEMP_7044_7,
            ["EVENT_2048_fade_in_from_black_async_12"],
            identifier="EVENT_2048_jmp_if_bit_set_11"),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(E2079_MONSTRO_TOWN_EXTERIOR_LOADER_FROM_SAVE_BOX),
        Jmp(["EVENT_2048_jmp_if_bit_clear_7"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2048_fade_in_from_black_async_12"
        ),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT,
            ["EVENT_2048_star_grant"],
            identifier="EVENT_2048_jmp_if_bit_clear_7"),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2048_star_grant"]),
        RunEventAsSubroutine(E3909_MONSTRO_STAR_PIECE_SIGNAL),
        JmpIfBitClear(GAMEBOY_KID_PURCHASE_COMPLETE, ["EVENT_2048_ret_26"]),
        JmpToEvent(
            E0168_BOSS_GRANT_STAR_PIECE_CONTAINER, identifier="EVENT_2048_star_grant"
        ),
        Return(identifier="EVENT_2048_ret_26"),
    ]
)
