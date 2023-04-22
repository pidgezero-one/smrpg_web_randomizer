# pylint: disable=C0301

"""E0506_PIPE_VAULT_SUMMON_FIRST_GOOMBA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_3, ["EVENT_256_ret_0"]),
        ClearBit(TEMP_7043_3),
        JmpIfObjectNotInSpecificLevel(
            NPC_3, R127_PIPE_VAULT_AREA_02, ["EVENT_506_summon_to_level_4"]
        ),
        Return(),
        SummonObjectToSpecificLevel(
            NPC_3, R127_PIPE_VAULT_AREA_02, identifier="EVENT_506_summon_to_level_4"
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=18, y=42, z=2, direction=EAST),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        SummonObjectToCurrentLevel(NPC_3),
        SetSyncActionScript(NPC_3, A0659_PIPE_VAULT_THWOMP_ROOM_GOOMBA),
        Return(),
    ]
)
