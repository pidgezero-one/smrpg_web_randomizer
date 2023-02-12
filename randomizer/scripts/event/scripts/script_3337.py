# E3337_CORKPEDITE_ANIMATION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7043_0, identifier="EVENT_3337_clear_bit_0"),
        Pause(1),
        JmpIfBitClear(TEMP_7043_4, ["EVENT_3337_set_bit_7"]),
        JmpIfBitClear(TEMP_7043_5, ["EVENT_3337_set_bit_7"]),
        JmpIfBitClear(TEMP_7043_6, ["EVENT_3337_set_bit_7"]),
        JmpIfBitClear(TEMP_7043_7, ["EVENT_3337_set_bit_7"]),
        Jmp(["EVENT_3337_clear_bit_0"]),
        SetBit(TEMP_7043_0, identifier="EVENT_3337_set_bit_7"),
        Pause(1, identifier="EVENT_3337_pause_8"),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3337_pause_8"]),
        Pause(8),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASDb(bytearray(b"\xfd\x9c\x15")),
                ASSetWalkingSpeed(FAST),
                ASStartLoopNTimes(23),
                ASShiftNorthPixels(2),
                ASShiftSouthPixels(2),
                ASEndLoop(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        JmpIfBitSet(TEMP_7043_4, ["EVENT_3337_jmp_if_bit_set_15"]),
        SetSyncActionScript(NPC_1, A0935_EJECTING_AN_OERLIKON),
        SetBit(TEMP_7043_4),
        JmpIfBitSet(
            TEMP_7043_5,
            ["EVENT_3337_jmp_if_bit_set_18"],
            identifier="EVENT_3337_jmp_if_bit_set_15",
        ),
        SetSyncActionScript(NPC_2, A0935_EJECTING_AN_OERLIKON),
        SetBit(TEMP_7043_5),
        JmpIfBitSet(
            TEMP_7043_6,
            ["EVENT_3337_jmp_if_bit_set_21"],
            identifier="EVENT_3337_jmp_if_bit_set_18",
        ),
        SetSyncActionScript(NPC_3, A0935_EJECTING_AN_OERLIKON),
        SetBit(TEMP_7043_6),
        JmpIfBitSet(
            TEMP_7043_7,
            ["EVENT_3337_pause_24"],
            identifier="EVENT_3337_jmp_if_bit_set_21",
        ),
        SetSyncActionScript(NPC_4, A0935_EJECTING_AN_OERLIKON),
        SetBit(TEMP_7043_7),
        Pause(16, identifier="EVENT_3337_pause_24"),
        Jmp(["EVENT_3337_clear_bit_0"]),
    ]
)
