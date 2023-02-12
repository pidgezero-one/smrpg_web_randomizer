# E3506_BOOSTER_HILL_GET_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_1, ["EVENT_3506_disable_trigger_2"]),
        Return(),
        DisableObjectTrigger(NPC_8, identifier="EVENT_3506_disable_trigger_2"),
        StopBackgroundEvent(TIMER_701C),
        EnableControlsUntilReturn([]),
        SetSyncActionScript(NPC_9, A0716_BOOSTER_HILL_BUMP_FLOWER),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        Add7000ToMaxFP(),
        Inc(BOOSTER_HILL_70B1),
        Pause(8),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetWalkingSpeed(FAST),
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
            ],
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASFixedFCoordOff(),
                ASPause(4),
                ASFaceSouthwest(),
                ASPause(4),
                ASFaceSoutheast(),
            ],
        ),
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
            ],
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASPause(4),
                ASFaceSouthwest(),
                ASPause(4),
                ASFaceNorthwest(),
                ASFixedFCoordOn(),
            ],
        ),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_3506_action_queue_async_16"]),
        SetSyncActionScript(NPC_7, A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASFloatingOff(),
                ASSetAllSpeeds(FAST),
                ASJumpToHeight(height=112, silent=True),
                ASSetSpriteSequence(
                    index=7, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASFloatingOn(),
                ASStartLoopNTimes(15),
                ASVisibilityOff(),
                ASPause(1),
                ASVisibilityOn(),
                ASShiftSoutheastPixels(1),
                ASDec(SECONDARY_TEMP_7024),
                ASEndLoop(),
                ASResetProperties(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
            identifier="EVENT_3506_action_queue_async_16",
        ),
        JmpIfBitClear(TEMP_7043_7, ["EVENT_3506_set_bit_19"]),
        SetTempSyncActionScript(NPC_7, A0718_BOOSTER_HILL_BOSS_MOVE_FORWARD),
        SetBit(TEMP_7043_7, identifier="EVENT_3506_set_bit_19"),
        EnableControlsUntilReturn([B]),
        ResumeBackgroundEvent(TIMER_701C),
        EnableObjectTrigger(NPC_8),
        Return(),
    ]
)
