# E3499_BOOSTER_HILL_1ST_PASS_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        SetVarToConst(TEMP_7034, 16),
        SetVarToConst(TEMP_7026, 1),
        SetVarToConst(BOOSTER_HILL_70B1, 0),
        FreezeCamera(),
        ActionQueueSync(
            target=MARIO, subscript=[ASTransferToXYZF(x=11, y=67, z=0, direction=EAST)]
        ),
        ActionQueueSync(
            target=LAYER_3,
            subscript=[ASSetWalkingSpeed(FAST), ASShiftNorthwestSteps(18)],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASDb(bytearray(b" \x04")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"(\x00\x00\x00\x00\x00\x80\x00\x01\x00\x01\x00\x00\x00 \x80"
                    )
                ),
                ASFixedFCoordOn(),
                ASSequenceLoopingOn(),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShiftZUpPixels(9),
                ASShiftSoutheastPixels(8),
            ],
        ),
        ActionQueueSync(target=NPC_8, subscript=[ASShiftNorthwestSteps(11)]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASShiftNorthwestSteps(11),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        SetSyncActionScript(NPC_8, A0715_FOREVER_PAUSE_LOOP),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_130"]),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_133"]),
        Pause(20),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_130"]),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_133"]),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_130"]),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_133"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASShiftNorthwestSteps(8),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_130"]),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_133"]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSequenceLoopingOn(),
                ASPause(40),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_130"]),
        ActionQueueSync(
            target=NPC_7, subscript=[ASSetSequenceSpeed(FAST), ASSequenceLoopingOn()]
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASSequenceLoopingOn()]),
        SetVarToConst(TEMP_70AE, 3),
        JmpToSubroutine(["EVENT_3499_action_queue_sync_133"]),
        SetSyncActionScript(NPC_3, A0707_BOOSTER_HILL_HENCHMAN),
        SetSyncActionScript(NPC_4, A0707_BOOSTER_HILL_HENCHMAN),
        SetSyncActionScript(NPC_5, A0707_BOOSTER_HILL_HENCHMAN),
        Pause(60),
        RunBackgroundEvent(
            event_id=E3500_BOOSTER_HILL_1ST_PASS_SNIFIT_JUMPS, return_on_level_exit=True
        ),
        RunBackgroundEvent(
            event_id=E3503_BOOSTER_HILL_BARREL_SUMMONER,
            return_on_level_exit=True,
            bit_6=True,
        ),
        SetSyncActionScript(LAYER_1, A0704_BOOSTER_HILL_LAYER_1),
        SetSyncActionScript(LAYER_2, A0655_BOOSTER_HILL_LAYER_2),
        SetSyncActionScript(LAYER_3, A0705_BOOSTER_HILL_LAYER_3),
        PlayMusicAtDefaultVolume(M38_BOOSTER_HILL),
        RunEventAtReturn(E3502_BOOSTER_HILL_END),
        Return(),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASShiftNorthPixels(4),
                ASSetSpriteSequence(
                    index=4, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASShiftNorthPixels(4),
                ASShiftWestPixels(8),
                ASSetSpriteSequence(
                    index=4,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShiftWestPixels(8),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
            ],
            identifier="EVENT_3499_action_queue_sync_130",
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASPause(4), ASFaceSouthwest(), ASPause(4), ASFaceSoutheast()],
        ),
        Return(),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASShiftEastPixels(8),
                ASSetSpriteSequence(
                    index=4, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASShiftEastPixels(8),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShiftSouthPixels(8),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
            ],
            identifier="EVENT_3499_action_queue_sync_133",
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASPause(4), ASFaceSouthwest(), ASPause(4), ASFaceNorthwest()],
        ),
        Return(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=5, y=54, z=0, direction=EAST),
                ASSetPriority(2),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(FASTER),
                ASShiftSouthwestPixels(36),
                ASPlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
                ASVisibilityOn(),
                ASJumpToHeight(
                    24,
                    identifier="EVENT_3499_action_queue_sync_136_SUBSCRIPT_jump_to_height_9",
                ),
                ASWalk1StepSoutheast(),
                ASSet700CToObjectCoord(object=DUMMY_0X07, coord=COORD_X, pixel=True),
                ASCompareVarToConst(PRIMARY_TEMP_700C, 5888),
                ASJmpIfComparisonResultIsLesser(
                    ["EVENT_3499_action_queue_sync_136_SUBSCRIPT_jump_to_height_9"]
                ),
            ],
        ),
        ActionQueueSync(target=NPC_3, subscript=[ASPause(50), ASJumpToHeight(112)]),
        Return(),
    ]
)
