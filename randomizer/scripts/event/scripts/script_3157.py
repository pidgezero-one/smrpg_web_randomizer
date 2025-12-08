# pylint: disable=C0301

"""E3157_MINECART_ROOM_LOADER_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_X,
            pixel=True,
            bit_7=True,
            identifier="EVENT_3157_set_7000_to_object_coord_0"),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 12, ["EVENT_3157_set_7000_to_object_coord_4"]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetVRAMPriority(NORMAL_PRIORITY), ASPause(1)],
            identifier="EVENT_3157_action_queue_async_2"),
        Jmp(["EVENT_3157_set_7000_to_object_coord_0"]),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Y,
            pixel=True,
            bit_7=True,
            identifier="EVENT_3157_set_7000_to_object_coord_4"),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 61, ["EVENT_3157_action_queue_async_2"]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASPause(1),
            ]),
        Jmp(["EVENT_3157_set_7000_to_object_coord_0"]),
    ]
)
