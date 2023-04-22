# pylint: disable=C0301

"""E3804_ENDING_CREDITS_CORONATION_NPCS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=MARIO, subscript=[ASVisibilityOff()]),
        SetTempSyncActionScript(NPC_2, A0803_INC_PALETTE_ROW),
        SetTempSyncActionScript(NPC_3, A0807_INC_PALETTE_ROW_2),
        SetTempSyncActionScript(NPC_7, A0804_INC_PALETTE_ROW_15),
        SetTempSyncActionScript(NPC_9, A0803_INC_PALETTE_ROW),
        SetTempSyncActionScript(NPC_5, A0807_INC_PALETTE_ROW_2),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                )
            ],
        ),
        StarMaskExpandFromScreenCenter(),
        Pause(60),
        SetTempSyncActionScript(NPC_8, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_1, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_3, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_11, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_9, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_2, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_7, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_5, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_10, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_6, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_4, A0238_CHEERING_NIMBITES),
        Pause(28),
        SetTempSyncActionScript(NPC_4, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_10, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_6, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_2, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_7, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_5, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_11, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_9, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_1, A0238_CHEERING_NIMBITES),
        SetTempSyncActionScript(NPC_3, A0238_CHEERING_NIMBITES),
        Pause(18),
        SetTempSyncActionScript(NPC_8, A0238_CHEERING_NIMBITES),
        Pause(65),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=15,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(20),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(20),
                ASSetSpriteSequence(
                    index=16,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(20),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(60),
                ASSetSpriteSequence(
                    index=17,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
            ],
        ),
        Pause(95),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(16),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(16),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASPause(18),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASPause(18),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_11,
            subscript=[
                ASPause(18),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASDb(bytearray(b" \x04")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80"
                    )
                ),
                ASWalkSouthwestPixels(8),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_14,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASDb(bytearray(b" \x04")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80"
                    )
                ),
                ASWalkSouthwestPixels(8),
                ASBPL262728(),
            ],
        ),
        Pause(45),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASDb(bytearray(b" \x04")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80"
                    )
                ),
                ASWalkNorthwestSteps(5),
            ],
        ),
        Pause(160),
        StarMaskShrinkToScreenCenter(),
        PauseScriptUntilEffectDone(),
        JmpToEvent(E3803_ENDING_CREDITS_GREEN_STAR),
    ]
)
