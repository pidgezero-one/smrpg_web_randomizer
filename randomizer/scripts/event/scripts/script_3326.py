# pylint: disable=C0301

"""E3326_STUMPET_ERUPTION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7043_0, identifier="EVENT_3326_clear_bit_0"),
        Pause(1),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 390, ["EVENT_3326_jmp_if_object_not_in_level_9"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_6, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_14"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_7, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_16"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_8, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_18"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_9, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_20"]
        ),
        Jmp(["EVENT_3326_clear_bit_0"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R390_VOLCANO_AREA_16_ERUPTING_STUMPET,
            ["EVENT_3326_set_14"],
            identifier="EVENT_3326_jmp_if_object_not_in_level_9",
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_7, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_16"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_8, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_18"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_9, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_20"]
        ),
        Jmp(["EVENT_3326_clear_bit_0"]),
        SetVarToConst(TEMP_70AA, 26, identifier="EVENT_3326_set_14"),
        Jmp(["EVENT_3326_pause_21"]),
        SetVarToConst(TEMP_70AA, 27, identifier="EVENT_3326_set_16"),
        Jmp(["EVENT_3326_pause_21"]),
        SetVarToConst(TEMP_70AA, 28, identifier="EVENT_3326_set_18"),
        Jmp(["EVENT_3326_pause_21"]),
        SetVarToConst(TEMP_70AA, 29, identifier="EVENT_3326_set_20"),
        Pause(60, identifier="EVENT_3326_pause_21"),
        CopyVarToVar(from_var=TEMP_70AA, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        SummonObjectAt70A8ToCurrentLevel(),
        SetBit(TEMP_7043_0),
        SetSyncActionScript(MEM_70AA, A0933_ERUPT),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASDb(bytearray(b"\xfd\x9c\x15")),
                ASStartLoopNTimes(33),
                ASWalkNorthPixels(1),
                ASWalkSouthPixels(1),
                ASEndLoop(),
            ],
        ),
        Pause(68),
        Jmp(["EVENT_3326_clear_bit_0"]),
    ]
)
