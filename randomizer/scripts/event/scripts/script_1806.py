# pylint: disable=C0301

"""E1806_TEMPLE_FORTUNE_RESULTS_DOG_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(BATTLE_PACK_ID, 83),
        StartBattleWithPackAt700E(),
        ClearBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1806_ret_10"]),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1806_ret_10"]),
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1806_ret_10"]),
        JmpToEvent(E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS),
        Return(identifier="EVENT_1806_ret_10"),
    ]
)
