# E0612_MARRYMORE_INN_2F_HALLWAY_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(BELLHOP_CALLED),
        JmpIfBitSet(EMPLOYMENT_704C_3, ["EVENT_612_clear_bit_12"]),
        JmpIfBitSet(
            TEMP_7042_0,
            ["EVENT_612_jmp_if_bit_set_5"],
            identifier="EVENT_612_jmp_if_bit_set_2",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfBitSet(
            TEMP_7042_1,
            ["EVENT_257_fade_in_from_black_async_0"],
            identifier="EVENT_612_jmp_if_bit_set_5",
        ),
        JmpIfBitSet(TEMP_7042_4, ["EVENT_257_fade_in_from_black_async_0"]),
        SetBit(TEMP_7042_1),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASTransferToXYZF(x=14, y=46, z=4, direction=EAST)]
        ),
        SetSyncActionScript(NPC_0, A0300_MARRYMORE_TOP_FLOOR_BELLHOP_MOVE_IF_WORKING),
        FadeInFromBlack(sync=False),
        Return(),
        ClearBit(EMPLOYMENT_704C_3, identifier="EVENT_612_clear_bit_12"),
        Jmp(["EVENT_612_jmp_if_bit_set_2"]),
    ]
)
