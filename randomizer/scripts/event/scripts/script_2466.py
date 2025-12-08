# pylint: disable=C0301

"""E2466_BEAN_VALLEY_1ST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_6, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_7, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_9, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_10, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        SummonObjectToSpecificLevel(NPC_11, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        ClearBit(DIRECTIONAL_7047_0),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4, ["EVENT_2466_set_7000_to_object_coord_19"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2466_action_queue_sync_33"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 7, ["EVENT_2466_set_7000_to_object_coord_22"]
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2466_action_queue_sync_25"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["EVENT_2466_action_queue_sync_29"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_2466_action_queue_sync_29"]),
        Jmp(["EVENT_2466_fade_in_from_black_async_36"]),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Y,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2466_set_7000_to_object_coord_19"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 70, ["EVENT_2466_action_queue_sync_33"]),
        Jmp(["EVENT_2466_action_queue_sync_25"]),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Y,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2466_set_7000_to_object_coord_22"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 75, ["EVENT_2466_action_queue_sync_33"]),
        Jmp(["EVENT_2466_action_queue_sync_25"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=8, y=112),
                ASJmpIfRandom1of2(
                    ["EVENT_2466_action_queue_sync_25_SUBSCRIPT_face_southeast_4"]
                ),
                ASFaceSouthwest(),
                ASReturn(),
                ASFaceSoutheast(
                    identifier="EVENT_2466_action_queue_sync_25_SUBSCRIPT_face_southeast_4"
                ),
            ],
            identifier="EVENT_2466_action_queue_sync_25"),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftToXYCoords(x=6, y=111),
                ASJmpIfRandom1of2(
                    ["EVENT_2466_action_queue_sync_26_SUBSCRIPT_face_southeast_4"]
                ),
                ASFaceSouthwest(),
                ASReturn(),
                ASFaceSoutheast(
                    identifier="EVENT_2466_action_queue_sync_26_SUBSCRIPT_face_southeast_4"
                ),
            ]),
        RemoveObjectFromCurrentLevel(NPC_1),
        Jmp(["EVENT_2466_fade_in_from_black_async_36"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=15, y=72),
                ASJmpIfRandom1of2(
                    ["EVENT_2466_action_queue_sync_29_SUBSCRIPT_face_southeast_4"]
                ),
                ASFaceSouthwest(),
                ASReturn(),
                ASFaceSoutheast(
                    identifier="EVENT_2466_action_queue_sync_29_SUBSCRIPT_face_southeast_4"
                ),
            ],
            identifier="EVENT_2466_action_queue_sync_29"),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=13, y=70),
                ASJmpIfRandom1of2(
                    ["EVENT_2466_action_queue_sync_30_SUBSCRIPT_face_southeast_4"]
                ),
                ASFaceSouthwest(),
                ASReturn(),
                ASFaceSoutheast(
                    identifier="EVENT_2466_action_queue_sync_30_SUBSCRIPT_face_southeast_4"
                ),
            ]),
        RemoveObjectFromCurrentLevel(NPC_2),
        Jmp(["EVENT_2466_fade_in_from_black_async_36"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftToXYCoords(x=5, y=72), ASFaceSoutheast()],
            identifier="EVENT_2466_action_queue_sync_33"),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=8, y=82),
                ASJmpIfRandom1of2(
                    ["EVENT_2466_action_queue_sync_34_SUBSCRIPT_face_southeast_4"]
                ),
                ASFaceSouthwest(),
                ASReturn(),
                ASFaceSoutheast(
                    identifier="EVENT_2466_action_queue_sync_34_SUBSCRIPT_face_southeast_4"
                ),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftToXYCoords(x=7, y=88),
                ASJmpIfRandom1of2(
                    ["EVENT_2466_action_queue_sync_35_SUBSCRIPT_face_southeast_4"]
                ),
                ASFaceSouthwest(),
                ASReturn(),
                ASFaceSoutheast(
                    identifier="EVENT_2466_action_queue_sync_35_SUBSCRIPT_face_southeast_4"
                ),
            ]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2466_fade_in_from_black_async_36"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2466_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2466_ret_26"]),
        RunEventAsSubroutine(E3911_BEAN_VALLEY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2466_ret_26"),
    ]
)
