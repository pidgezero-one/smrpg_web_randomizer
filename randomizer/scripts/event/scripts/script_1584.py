# E1584_TEMPLE_FINAL_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASShiftEastPixels(11),
                ASShiftNortheastPixels(4),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_1584_set_bit_0"]),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromSpecificLevel(
            NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
        ),
        JmpIfBitSet(
            TEMPLE_BOSS_DEFEATED,
            ["EVENT_1584_summon_to_level_248"],
            identifier="EVENT_1584_set_bit_0",
        ),
        ActionQueueAsync(
            target=NPC_1, subscript=[ASShiftWestPixels(8), ASShiftSouthPixels(8)]
        ),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASShiftWestPixels(8), ASShiftSouthPixels(8)]
        ),
        Jmp(["EVENT_1584_set_0"]),
        RemoveObjectFromSpecificLevel(
            NPC_1,
            R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN,
            identifier="EVENT_1584_summon_to_level_248",
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromSpecificLevel(
            NPC_2, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 37, identifier="EVENT_1584_set_0"),
        JmpIfBitClear(TEMP_708C_4, ["EVENT_1584_jmp_if_bit_clear_3"]),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 43),
        JmpIfBitClear(
            LANDS_END_CHEST_2_REQUESTED,
            ["EVENT_1584_jmp_if_bit_set_5"],
            identifier="EVENT_1584_jmp_if_bit_clear_3",
        ),
        SummonObjectToSpecificLevel(
            NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        JmpIfBitSet(
            TEMP_7044_6,
            ["EVENT_1584_set_bit_8"],
            identifier="EVENT_1584_jmp_if_bit_set_5",
        ),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_1584_jmp_if_bit_clear_7"]),
        SetBit(HAS_A_PRIZE_FORTUNE, identifier="EVENT_1584_set_bit_8"),
        ClearBit(BELOME_FORTUNE_1),
        ClearBit(UNKNOWN_BELOME_FORTUNE),
        ClearBit(UNKNOWN_BELOME_TEMPLE),
        SetVarToConst(TEMP_70AC, 0),
        ClearBit(FLOWER_TOWER_ASCENDED),
        ClearBit(SKY_BRIDGE_TUTORIAL_BIT),
        SetVarToConst(UNKNOWN_70AD, 0),
        RemoveObjectFromCurrentLevel(NPC_0),
        SetBit(TEMPLE_ELEVATOR_DIRECTION),
        SummonObjectToSpecificLevel(NPC_0, R263_LANDS_END_UNDERGROUND_AREA_01),
        SummonObjectToSpecificLevel(NPC_1, R263_LANDS_END_UNDERGROUND_AREA_01),
        SummonObjectToSpecificLevel(NPC_2, R263_LANDS_END_UNDERGROUND_AREA_01),
        SummonObjectToSpecificLevel(NPC_0, R264_LANDS_END_UNDERGROUND_AREA_02),
        SummonObjectToSpecificLevel(NPC_1, R264_LANDS_END_UNDERGROUND_AREA_02),
        SummonObjectToSpecificLevel(NPC_2, R264_LANDS_END_UNDERGROUND_AREA_02),
        SummonObjectToSpecificLevel(NPC_0, R265_LANDS_END_UNDERGROUND_AREA_03),
        SummonObjectToSpecificLevel(NPC_1, R265_LANDS_END_UNDERGROUND_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R265_LANDS_END_UNDERGROUND_AREA_03),
        SummonObjectToSpecificLevel(
            NPC_0, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_7, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_8, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_9, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_10, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_11, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_12, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_13, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_14, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_15, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        FadeInFromBlack(sync=True),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT,
            ["EVENT_1584_ret_26"],
            identifier="EVENT_1584_jmp_if_bit_clear_7",
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1584_ret_26"]),
        RunEventAsSubroutine(E3908_TEMPLE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1584_ret_26"),
    ]
)
