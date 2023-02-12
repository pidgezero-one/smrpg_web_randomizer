# E3500_BOOSTER_HILL_1ST_PASS_SNIFIT_JUMPS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_3500_pause_0"),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3500_jmp_if_bit_clear_4"]),
        ActionQueueSync(target=NPC_3, subscript=[ASJumpToHeight(104)]),
        ClearBit(TEMP_7043_0),
        JmpIfBitClear(
            TEMP_7043_1,
            ["EVENT_3500_jmp_if_bit_clear_7"],
            identifier="EVENT_3500_jmp_if_bit_clear_4",
        ),
        ActionQueueSync(target=NPC_4, subscript=[ASJumpToHeight(104)]),
        ClearBit(TEMP_7043_1),
        JmpIfBitClear(
            TEMP_7043_2,
            ["EVENT_3500_pause_0"],
            identifier="EVENT_3500_jmp_if_bit_clear_7",
        ),
        ActionQueueSync(target=NPC_5, subscript=[ASJumpToHeight(104)]),
        ClearBit(TEMP_7043_2),
        Jmp(["EVENT_3500_pause_0"]),
    ]
)
