# E3094_STAR_PIECE_CHEST_ANIMATION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        DisableTriggerOfObjectAt70A8InCurrentLevel(),
        SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
        Set70107015ToObjectXYZ(MEM_70A8),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        JmpIfBitSet(UNKNOWN_704A_3, ["EVENT_3094_clear_bit_10"]),
        PlaySound(sound=SO081_STAR, channel=6),
        ClearBit(UNKNOWN_704A_3, identifier="EVENT_3094_clear_bit_10"),
        CreatePacketAt7010(
            packet=P081_STAR_PIECE_CHEST, destinations=["EVENT_3094_ret_12"]
        ),
        Pause(45),
        Return(identifier="EVENT_3094_ret_12"),
    ]
)
