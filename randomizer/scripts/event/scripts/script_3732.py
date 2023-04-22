# pylint: disable=C0301

"""E3732_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(
            INNER_FACTORY_ROOM_2_COMPLETED, ["EVENT_3732_action_queue_async_2"]
        ),
        SummonObjectToCurrentLevel(NPC_6),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)],
            identifier="EVENT_3732_action_queue_async_2",
        ),
        RunEventAsSubroutine(
            E0839_NIMBUS_CASTLE_SECOND_POST_THRONE_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(TEMP_7076_0, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_3584_ret_0"]),
        ClearBit(EXP_STAR_BIT_6),
        CreatePacketAtObjectCoords(
            packet=P022_RECURSIVE_SPARKLES,
            target_npc=MARIO,
            destinations=["EVENT_3584_ret_0"],
        ),
        Return(),
    ]
)
