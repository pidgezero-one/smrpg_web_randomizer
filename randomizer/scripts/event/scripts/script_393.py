# E0393_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0770_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            ["EVENT_393_set_bit_16"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            ["EVENT_393_set_bit_16"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ["EVENT_393_summon_to_current_level_4"],
        ),
        JmpIfBitSet(
            OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED,
            ["EVENT_393_jmp_if_object_not_in_level_27"],
        ),
        SummonObjectToCurrentLevel(
            NPC_0, identifier="EVENT_393_summon_to_current_level_4"
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=7, y=22, z=4, direction=EAST),
                ASFaceNorthwest(),
            ],
        ),
        PauseActionScript(NPC_0),
        SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=7, y=16, z=4, direction=EAST),
                ASFaceNortheast(),
            ],
            identifier="EVENT_393_action_queue_sync_8",
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=5, y=18, z=4, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        RememberLastObject(),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        SetSyncActionScript(NPC_1, A0119_SLOW_SEQUENCE_LOOP),
        SetSyncActionScript(NPC_2, A0128_WALK_RANDOM_DIRECTIONS),
        Jmp(["EVENT_261_1"]),
        SetBit(TEMP_7043_3, identifier="EVENT_393_set_bit_16"),
        PauseActionScript(NPC_0),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        ActionQueueSync(target=NPC_0, subscript=[ASFixedFCoordOn()]),
        ActionQueueSync(target=NPC_1, subscript=[ASFixedFCoordOn()]),
        ActionQueueSync(target=NPC_2, subscript=[ASFixedFCoordOn()]),
        SetSyncActionScript(NPC_0, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        SetSyncActionScript(NPC_1, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        SetSyncActionScript(NPC_2, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        Jmp(["EVENT_261_1"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ["EVENT_393_summon_to_current_level_4"],
            identifier="EVENT_393_jmp_if_object_not_in_level_27",
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        Jmp(["EVENT_393_action_queue_sync_8"]),
    ]
)
