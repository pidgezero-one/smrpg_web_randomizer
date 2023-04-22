# pylint: disable=C0301

"""E1688_TEMPLE_FORTUNE_HEADS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1688_remove_from_level_6_"]),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_1688_remove_from_level_6_"]
        ),
        JmpIfBitSet(BELOME_FORTUNE_1, ["EVENT_1688_remove_from_level_6_"]),
        SummonObjectToSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
        Jmp(["EVENT_1688_mem_7000_and_const_3"]),
        RemoveObjectFromSpecificLevel(
            NPC_3,
            R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            identifier="EVENT_1688_remove_from_level_6_",
        ),
        Mem7000AndConst(0x0003, identifier="EVENT_1688_mem_7000_and_const_3"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x000C),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        JmpIf7000AllBitsClear(
            bits=[], destinations=["EVENT_1688_jmp_if_7000_all_bits_clear_12"]
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            mod_id=32,
        ),
        SetBit(BELOME_HEAD_1),
        JmpIf7000AllBitsClear(
            bits=[],
            destinations=["EVENT_1688_jmp_if_7000_all_bits_clear_15"],
            identifier="EVENT_1688_jmp_if_7000_all_bits_clear_12",
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            mod_id=33,
        ),
        SetBit(BELOME_HEAD_2),
        JmpIf7000AllBitsClear(
            bits=[],
            destinations=["EVENT_1688_jmp_if_bit_clear_18"],
            identifier="EVENT_1688_jmp_if_7000_all_bits_clear_15",
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            mod_id=34,
        ),
        SetBit(BELOME_HEAD_3),
        JmpIfBitClear(
            UNKNOWN_BELOME_FORTUNE,
            ["EVENT_1688_jmp_to_event_23"],
            identifier="EVENT_1688_jmp_if_bit_clear_18",
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASWalkSouthPixels(4),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASPause(
                    1, identifier="EVENT_1688_action_queue_sync_19_SUBSCRIPT_pause_8"
                ),
                ASJmpIfObjectInAir(
                    NPC_0, ["EVENT_1688_action_queue_sync_19_SUBSCRIPT_pause_8"]
                ),
                ASWalkNorthPixels(8),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASWalkSouthPixels(4),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASPause(
                    1, identifier="EVENT_1688_action_queue_async_20_SUBSCRIPT_pause_8"
                ),
                ASJmpIfObjectInAir(
                    NPC_1, ["EVENT_1688_action_queue_async_20_SUBSCRIPT_pause_8"]
                ),
                ASWalkNorthPixels(8),
            ],
        ),
        JmpIfBitClear(UNKNOWN_BELOME_TEMPLE, ["EVENT_1688_jmp_to_event_23"]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASIncPaletteRowBy(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASWalkSouthPixels(4),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASPause(10),
            ],
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1688_jmp_to_event_23"),
    ]
)
