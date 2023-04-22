# pylint: disable=C0301

"""E3360_KEEP_COIN_GAME_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(NPC_2),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        Dec(ROSE_WAY_703C),
        JmpIfLoadedMemoryIsNot0(["EVENT_3360_set_temp_action_script_sync_6"]),
        SetSyncActionScript(NPC_2, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
        Jmp(["EVENT_3360_set_7010_to_object_xyz_7"]),
        SetTempSyncActionScript(
            NPC_2,
            A0008_HIT_TREASURE_CHEST_CONTENTS_REMAINING,
            identifier="EVENT_3360_set_temp_action_script_sync_6",
        ),
        Set70107015ToObjectXYZ(NPC_2, identifier="EVENT_3360_set_7010_to_object_xyz_7"),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        PlaySound(sound=SO013_COIN, channel=4),
        CreatePacketAt7010(
            packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_3360_ret_14"]
        ),
        SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
        Return(identifier="EVENT_3360_ret_14"),
    ]
)
