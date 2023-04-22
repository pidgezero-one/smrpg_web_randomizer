"""A0344_SHIP_PUZZLE_AREA_GREAPERS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        Mem700CAndConst(0x0007),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C, 3, ["ACTION_344_sequence_looping_on_4"]
        ),
        ShiftXYPixels(x=9, y=8),
        SequenceLoopingOn(identifier="ACTION_344_sequence_looping_on_4"),
        FixedFCoordOn(),
        Set700CToPressedButton(),
        Mem700CAndConst(0x0007),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_344_pause_22"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_344_pause_21"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_344_pause_20"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_344_pause_19"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_344_pause_18"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_344_pause_17"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_344_pause_16"]),
        Pause(2),
        Pause(2, identifier="ACTION_344_pause_16"),
        Pause(2, identifier="ACTION_344_pause_17"),
        Pause(2, identifier="ACTION_344_pause_18"),
        Pause(2, identifier="ACTION_344_pause_19"),
        Pause(2, identifier="ACTION_344_pause_20"),
        Pause(2, identifier="ACTION_344_pause_21"),
        Pause(1, identifier="ACTION_344_pause_22"),
        Jmp(["ACTION_344_pause_22"]),
    ]
)
