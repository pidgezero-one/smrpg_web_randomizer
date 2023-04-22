# pylint: disable=C0301

"""E1732_SKY_BRIDGE_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_3, identifier="EVENT_1732_set_bit_0"),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        SetSyncActionScript(NPC_11, A0047_SKY_BRIDGE_BULLET_BILL),
        ClearBit(TEMP_7044_5),
        Pause(1, identifier="EVENT_1732_pause_4"),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_1732_pause_4"]),
        JmpIfObjectInCurrentLevel(NPC_12, ["EVENT_1732_set_object_memory_to_8"]),
        Jmp(["EVENT_1732_pause_4"]),
        SetObjectMemoryToVar(TEMP_702C, identifier="EVENT_1732_set_object_memory_to_8"),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_12, A0047_SKY_BRIDGE_BULLET_BILL),
        ClearBit(TEMP_7044_5),
        Pause(1, identifier="EVENT_1732_pause_13"),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_1732_pause_13"]),
        JmpIfObjectInCurrentLevel(NPC_13, ["EVENT_1732_set_object_memory_to_17"]),
        Jmp(["EVENT_1732_pause_13"]),
        SetObjectMemoryToVar(
            TEMP_702C, identifier="EVENT_1732_set_object_memory_to_17"
        ),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_13, A0047_SKY_BRIDGE_BULLET_BILL),
        ClearBit(TEMP_7044_5),
        Pause(1, identifier="EVENT_1732_pause_22"),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_1732_pause_22"]),
        JmpIfObjectInCurrentLevel(NPC_14, ["EVENT_1732_set_object_memory_to_26"]),
        Jmp(["EVENT_1732_pause_22"]),
        SetObjectMemoryToVar(
            TEMP_702C, identifier="EVENT_1732_set_object_memory_to_26"
        ),
        Pause(1),
        EndLoop(),
        SetSyncActionScript(NPC_14, A0047_SKY_BRIDGE_BULLET_BILL),
        ClearBit(TEMP_7044_5),
        Pause(1, identifier="EVENT_1732_pause_31"),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_1732_pause_31"]),
        JmpIfObjectInCurrentLevel(NPC_11, ["EVENT_1732_action_queue_async_35"]),
        Jmp(["EVENT_1732_pause_31"]),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
            identifier="EVENT_1732_action_queue_async_35",
        ),
        ClearBit(TEMP_7044_3),
        SetObjectMemoryToVar(TEMP_702C),
        Pause(1),
        EndLoop(),
        Pause(20),
        Pause(1, identifier="EVENT_1732_pause_41"),
        JmpIfBitSet(TEMP_7044_1, ["EVENT_1732_pause_41"]),
        Jmp(["EVENT_1732_set_bit_0"]),
    ]
)
