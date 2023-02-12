# E3950_POST_FINAL_BOSS_INIT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            face_direction=SOUTHWEST,
            x=4,
            y=51,
            z=0,
        ),
        FreezeCamera(),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=3, y=50, z=0, direction=EAST),
                ASTransferXYZFPixels(x=248, y=0, z=0, direction=EAST),
                ASFaceSoutheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=6, y=57, z=0, direction=EAST),
                ASTransferXYZFPixels(x=240, y=0, z=0, direction=EAST),
                ASSetSpriteSequence(
                    index=23,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(2),
                ASResetProperties(),
                ASFaceNorthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=3, y=56, z=0, direction=EAST),
                ASTransferXYZFPixels(x=240, y=0, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=4, y=53, z=0, direction=EAST),
                ASTransferXYZFPixels(x=242, y=252, z=0, direction=EAST),
                ASSetSpriteSequence(index=6, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=6, y=50, z=0, direction=EAST),
                ASTransferXYZFPixels(x=240, y=254, z=0, direction=EAST),
            ],
        ),
        FadeInFromColour(duration=40, colour=WHITE),
        PauseScriptUntilEffectDone(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepSouthwest(),
                ASShiftSouthwestPixels(12),
                ASSetSpriteSequence(
                    index=12, sprite_offset=6, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(30),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNorthwest(),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNorthwest(),
                ASShiftNorthwestPixels(8),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(16),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepSoutheast(),
                ASShiftSoutheastPixels(8),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(16),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNortheast(),
                ASShiftNortheastPixels(6),
                ASSetSpriteSequence(
                    index=7, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        RememberLastObject(),
        Pause(120),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=4, y=56, z=0, direction=EAST),
                ASTransferXYZFPixels(x=2, y=220, z=0, direction=EAST),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASVisibilityOn(),
                ASSequenceLoopingOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASStartLoopNTimes(1),
                ASPause(60),
                ASShiftZUpPixels(12),
                ASShiftZDownPixels(12),
                ASEndLoop(),
                ASPause(60),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASPause(56),
                ASVisibilityOff(),
                ASSetPriority(0),
                ASTransferXYZFPixels(x=0, y=216, z=0, direction=EAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASVisibilityOn(),
                ASSetPriority(2),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(90),
                ASResetProperties(),
                ASPause(150),
                ASSetSpriteSequence(
                    index=9, sprite_offset=2, is_sequence=True, looping=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(120),
                ASResetProperties(),
                ASPause(90),
                ASSetSpriteSequence(
                    index=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(90),
                ASResetProperties(),
                ASPause(120),
                ASSetSpriteSequence(
                    index=22,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(2),
                ASSetSpriteSequence(
                    index=23,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASPause(90),
                ASResetProperties(),
                ASPause(120),
                ASSetSpriteSequence(
                    index=22,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(2),
                ASSetSpriteSequence(
                    index=23,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        RememberLastObject(),
        SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
        Pause(90),
        PauseActionScript(NPC_6),
        StartAsyncEmbeddedActionScript(
            target=NPC_6,
            prefix=0xF1,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASBPL262728(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"%\x00\x07\x80\xff")),
                ASDb(bytearray(b"$\x98\xff\xc8\xff")),
                ASPause(30),
                ASBPL262728(),
            ],
        ),
        SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetSpriteSequence(
                    index=18,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASResetProperties()]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=8, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        Pause(60),
        PauseActionScript(NPC_6),
        StartAsyncEmbeddedActionScript(
            target=NPC_6,
            prefix=0xF1,
            subscript=[
                ASBPL262728(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"%\x80\x06\xa0\xff")),
                ASDb(bytearray(b"$\x90\xff\x00\x01")),
                ASPause(30),
            ],
        ),
        SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=19, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        ActionQueueSync(target=MARIO, subscript=[ASResetProperties()]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        Pause(60),
        PauseActionScript(NPC_6),
        StartAsyncEmbeddedActionScript(
            target=NPC_6,
            prefix=0xF1,
            subscript=[
                ASBPL262728(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"%\xc0\x06\x88\xff")),
                ASDb(bytearray(b"$x\x01\x00\x00")),
                ASPause(28),
            ],
        ),
        SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=9, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=5, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=48, silent=True),
                ASPause(
                    1, identifier="EVENT_3950_action_queue_async_265_SUBSCRIPT_pause_2"
                ),
                ASJmpIfObjectInAir(
                    NPC_0, ["EVENT_3950_action_queue_async_265_SUBSCRIPT_pause_2"]
                ),
                ASSetSpriteSequence(
                    index=2, sprite_offset=2, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(60),
        PauseActionScript(NPC_6),
        StartAsyncEmbeddedActionScript(
            target=NPC_6,
            prefix=0xF1,
            subscript=[
                ASBPL262728(),
                ASDb(bytearray(b" \x07")),
                ASDb(bytearray(b"%\x80\x06\x90\xff")),
                ASDb(bytearray(b"$ \x000\xff")),
                ASPause(30),
            ],
        ),
        SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=9, sprite_offset=2, is_sequence=True, looping=True
                )
            ],
        ),
        Pause(60),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=4, y=52, z=0, direction=EAST),
                ASTransferXYZFPixels(x=242, y=252, z=0, direction=EAST),
            ],
        ),
        SetSyncActionScript(NPC_5, A0228_ENDING_CUTSCENE_EFFECT),
        Pause(2),
        PauseActionScript(NPC_6),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[ASBPL262728(), ASSetObjectMemoryBits(arg_1=0x0E, bits=[0])],
        ),
        Pause(230),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftNorthSteps(3),
                ASShiftNorthPixels(8),
                ASPause(2),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthSteps(6),
            ],
        ),
        Pause(240),
        JmpToEvent(E3951_STAR_PIECE_CREDITS_INIT),
    ]
)
