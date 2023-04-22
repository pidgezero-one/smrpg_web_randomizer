"""A0665_PIPE_VAULT_PIRANHA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(identifier="ACTION_665_shadow_off_0"),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Pause(60),
        Pause(90, identifier="ACTION_665_pause_3"),
        Pause(1, identifier="ACTION_665_pause_4"),
        JmpIfBitClear(TEMP_7044_3, ["ACTION_665_visibility_on_7"]),
        Jmp(["ACTION_665_shadow_off_0"]),
        VisibilityOn(identifier="ACTION_665_visibility_on_7"),
        SetPriority(3),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        AddZCoord1Step(),
        ShiftZUpPixels(12),
        SetSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(48),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        DecZCoord1Step(),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ShiftZDownPixels(12),
        VisibilityOff(),
        JmpIfRandom2of3(["ACTION_665_pause_3", "ACTION_665_pause_4"]),
        Jmp(["ACTION_665_shadow_off_0"]),
    ]
)
