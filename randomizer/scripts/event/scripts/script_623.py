# E0623_MARRYMORE_INN_EMPLOYED_GUEST_LEAVES

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom1of2(["EVENT_623_pause_2"]),
        Pause(90),
        Pause(60, identifier="EVENT_623_pause_2"),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_623_set_action_script_sync_12"]
        ),
        SetSyncActionScript(NPC_7, A0327_MARRYMORE_ELDERLY_GUEST_LEAVES),
        Jmp(["EVENT_623_pause_13"]),
        SetSyncActionScript(
            NPC_6,
            A0327_MARRYMORE_ELDERLY_GUEST_LEAVES,
            identifier="EVENT_623_set_action_script_sync_12",
        ),
        Pause(1, identifier="EVENT_623_pause_13"),
        JmpIfBitSet(TEMP_7044_3, ["EVENT_623_set_7000_to_object_coord_16"]),
        Jmp(["EVENT_623_pause_13"]),
        Set7000ToObjectCoord(
            object=NPC_5,
            coord=COORD_Y,
            pixel=True,
            bit_7=True,
            identifier="EVENT_623_set_7000_to_object_coord_16",
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 63, ["EVENT_623_unsync_action_script_19"]
        ),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalk1StepNortheast(),
                ASFaceNorthwest(),
            ],
        ),
        UnsyncActionScript(NPC_9, identifier="EVENT_623_unsync_action_script_19"),
        UnsyncActionScript(NPC_8),
        UnsyncActionScript(NPC_6),
        UnsyncActionScript(NPC_7),
        ClearBit(GUEST_DROPPED_OFF),
        Return(),
    ]
)
