"""A0639_ROSE_TOWN_ARROW_THAT_FREEZES_TOAD_BY_INN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_700C),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=X_COORD_2),
        CopyVarToVar(from_var=ROSE_TOWN_ARROW_POSITION, to_var=PRIMARY_TEMP_700C),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=Y_COORD_2),
        SetVarToConst(Z_COORD_2, 32),
        Db(bytearray(b"\x9a")),
        JmpIfBitSet(TEMP_7043_0, ["ACTION_639_transfer_xyzf_pixels_9"]),
        TransferXYZFPixels(x=212, y=6, z=30, direction=NORTHEAST),
        Jmp(["ACTION_639_visibility_on_10"]),
        TransferXYZFPixels(
            x=244,
            y=14,
            z=30,
            direction=NORTHEAST,
            identifier="ACTION_639_transfer_xyzf_pixels_9"),
        VisibilityOn(identifier="ACTION_639_visibility_on_10"),
        Jmp(["ACTION_638_set_bit_4"]),
    ]
)
