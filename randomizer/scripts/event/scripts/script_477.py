# E0477_DISMOUNT_YOSHI_1

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_5, ["EVENT_256_ret_0"]),
        Db(bytearray(b"\xfdE")),
        ActionQueueSync(
            target=NPC_9, subscript=[ASFaceNortheast(), ASSetSequenceSpeed(FAST)]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetWalkingSpeed(SLOW),
                ASBounceToXYWithHeight(x=8, y=85, height=0),
                ASFaceNortheast(),
            ],
        ),
        PauseActionScript(NPC_9),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[]),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        ClearBit(TEMP_7044_0),
        ClearBit(TEMP_7044_1),
        ClearBit(TEMP_7044_2),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7044_5),
        SetVarToConst(ROSE_WAY_703E, 3),
        SetSyncActionScript(NPC_9, A0289_MARIO_DISMOUNT_YOSHI),
        SetAsyncActionScript(MARIO, A0288_MARIO_DISMOUNT_YOSHI),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASSetSolidityBits(cant_walk_through=True)]
        ),
        ClearBit(TEMP_7044_4),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
