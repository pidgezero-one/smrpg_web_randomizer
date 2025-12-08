# pylint: disable=C0301

"""E3410_FROG_COIN_CHEST_MULTI_HIT_6"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        JmpIfVarEqualsConst(ITEM_ID, 240, ["EVENT_3410_play_sound_3"]),
        DisableTriggerOfObjectAt70A8InCurrentLevel(),
        PlaySound(
            sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_3410_play_sound_3"
        ),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        SetVarToConst(PRIMARY_TEMP_7000, 293),
        JmpIfMem704XAt7000BitSet(["EVENT_3410_jmp_if_var_not_equals_const_26"]),
        SetMem704XAt7000Bit(),
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x000F),
        JmpIfVarEqualsConst(
            COIN_CHEST_MULTIPLIER,
            0,
            ["EVENT_3410_set_70A0_short_mem_to_7000_16"],
            identifier="EVENT_3410_check_multiplier"),
        AddConstToVar(PRIMARY_TEMP_7000, 15),
        Dec(COIN_CHEST_MULTIPLIER),
        Jmp(["EVENT_3410_check_multiplier"]),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=CURRENT_OVERWORLD_MARKER_ID,
            identifier="EVENT_3410_set_70A0_short_mem_to_7000_16"),
        JmpIfVarNotEqualsConst(
            CURRENT_OVERWORLD_MARKER_ID,
            1,
            ["EVENT_3410_set_temp_action_script_sync_35"],
            identifier="EVENT_3410_jmp_if_var_not_equals_const_26"),
        SetSyncActionScript(MEM_70AA, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
        SetVarToConst(PRIMARY_TEMP_7000, 293),
        ClearMem704XAt7000Bit(),
        Jmp(["EVENT_3410_set_7010_to_object_xyz_36"]),
        SetTempSyncActionScript(
            MEM_70AA,
            A0008_HIT_TREASURE_CHEST_CONTENTS_REMAINING,
            identifier="EVENT_3410_set_temp_action_script_sync_35"),
        Set70107015ToObjectXYZ(
            MEM_70AA, identifier="EVENT_3410_set_7010_to_object_xyz_36"
        ),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        Dec(CURRENT_OVERWORLD_MARKER_ID),
        AddFrogCoins(1),
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        CreatePacketAt7010(
            packet=P019_FROG_COIN_BEING_COLLECTED, destinations=["EVENT_3410_ret_80"]
        ),
        SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
        Return(identifier="EVENT_3410_ret_80"),
    ]
)
