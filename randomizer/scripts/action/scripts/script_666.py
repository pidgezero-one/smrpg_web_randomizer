"""A0666_PIPE_VAULT_PIRANHA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(identifier="ACTION_666_shadow_off_0"),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Pause(60),
        Pause(1, identifier="ACTION_666_pause_3"),
        JmpIfBitClear(TEMP_7044_4, ["ACTION_666_visibility_on_6"]),
        Jmp(["ACTION_666_shadow_off_0"]),
        VisibilityOn(identifier="ACTION_666_visibility_on_6"),
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
        JmpIfRandom1of2(["ACTION_666_pause_3"]),
        Jmp(["ACTION_666_shadow_off_0"]),
    ]
)
