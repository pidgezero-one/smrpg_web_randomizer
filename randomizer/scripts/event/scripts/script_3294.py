# E3294_SHIP_BULLET_COLLISION_BACKGROUND

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([]),
        ClearBit(TEMP_7044_7),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASSetWalkingSpeed(FAST),
                ASSet700CToObjectCoord(object=MEM_70AA, coord=COORD_F, pixel=True),
                ASMem700CAndConst(0x000F),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    ["EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_6"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    3,
                    ["EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_10"],
                ),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_6",
                ),
                ASShiftSoutheastPixels(2),
                ASJmpIfMarioInAir(
                    ["EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_bit_14"]
                ),
                ASJmp(
                    ["EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_6"]
                ),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_10",
                ),
                ASShiftSouthwestPixels(2),
                ASJmpIfMarioInAir(
                    ["EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_bit_14"]
                ),
                ASJmp(
                    ["EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_10"]
                ),
                ASSetBit(
                    TEMP_7044_7,
                    identifier="EVENT_3294_action_queue_sync_2_SUBSCRIPT_set_bit_14",
                ),
                ASResetProperties(),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZDownPixels(1),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASReturn(),
            ],
        ),
        Pause(1, identifier="EVENT_3294_pause_3"),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3294_pause_3"]),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
