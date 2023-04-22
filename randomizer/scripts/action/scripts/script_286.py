"""A0286_KEEP_THWOMPS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOff(),
        ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
        ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
        SetWalkingSpeed(FAST),
        SetPriority(2),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        VarShiftLeft(PRIMARY_TEMP_700C, 255),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(23),
        EndLoop(),
        FloatingOn(identifier="ACTION_286_floating_on_11"),
        JumpToHeight(height=0, silent=True),
        Pause(1, identifier="ACTION_286_pause_13"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_286_pause_13"]),
        ShadowOff(),
        PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 4),
        SetMem704XAt700CBit(),
        Pause(20),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 4),
        ClearMem704XAt700CBit(),
        ShadowOn(),
        SetWalkingSpeed(VERY_FAST, identifier="ACTION_286_set_animation_speed_25"),
        ShiftZUpPixels(2),
        Set700CToObjectCoord(
            target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True, bit_7=True
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C, 16, ["ACTION_286_set_animation_speed_25"]
        ),
        Pause(110),
        Jmp(["ACTION_286_floating_on_11"]),
    ]
)
