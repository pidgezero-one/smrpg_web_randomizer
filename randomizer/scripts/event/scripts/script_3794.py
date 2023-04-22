# pylint: disable=C0301

"""E3794_FACTORY_FINAL_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(NPC_9, A0991_SMITHY_COMPONENT),
        SetSyncActionScript(NPC_4, A0240_SMITHY_COMPONENT),
        SetSyncActionScript(NPC_8, A0990_SMITHY_COMPONENT),
        SetSyncActionScript(NPC_5, A0241_SMITHY_COMPONENT),
        SetBit(TEMP_7044_0),
        RunBackgroundEvent(
            event_id=E3793_FACTORY_SMELTER_ANIMATION, return_on_level_exit=True
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(["EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_2"]),
                ASPlaySound(sound=SO058_INSERT, channel=4),
                ASSetSpriteSequence(
                    index=0, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASPause(30),
                ASResetProperties(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASPause(30), ASSetWalkingSpeed(FAST), ASWalk1StepSouth()],
        ),
        RememberLastObject(),
        Pause(10),
        UnsyncActionScript(NPC_9),
        UnsyncActionScript(NPC_4),
        UnsyncActionScript(NPC_5),
        UnsyncActionScript(NPC_8),
        Pause(1, identifier="EVENT_3794_pause_23"),
        JmpIfBitClear(TEMP_704C_0, ["EVENT_3794_pause_23"]),
        ClearBit(TEMP_704C_0),
        StopAllBackgroundEvents(),
        SetBit(TEMP_7043_2),
        SetSyncActionScript(NPC_4, A0989_SMITHY_COMPONENT),
        SetSyncActionScript(NPC_9, A0988_SMITHY_COMPONENT),
        JmpToSubroutine(["EVENT_3794_set_bit_144"]),
        Pause(10),
        JmpToSubroutine(["EVENT_3794_set_bit_149"]),
        SetBit(TEMP_7043_5),
        SetBit(TEMP_7043_1),
        RunBackgroundEvent(
            event_id=E3793_FACTORY_SMELTER_ANIMATION, return_on_level_exit=True
        ),
        Pause(90),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(30),
                ASResetProperties(),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        Pause(60),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(80),
                ASPause(
                    1, identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_1"]
                ),
                ASJumpToHeight(80),
                ASPause(
                    1, identifier="EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_4"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3794_action_queue_async_51_SUBSCRIPT_pause_4"]
                ),
            ],
        ),
        Pause(30),
        UnsyncActionScript(NPC_9),
        UnsyncActionScript(NPC_4),
        UnsyncActionScript(NPC_5),
        UnsyncActionScript(NPC_8),
        Pause(1, identifier="EVENT_3794_pause_57"),
        JmpIfBitClear(TEMP_704C_0, ["EVENT_3794_pause_57"]),
        ClearBit(TEMP_704C_0),
        StopAllBackgroundEvents(),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_5),
        SetSyncActionScript(NPC_4, A0989_SMITHY_COMPONENT),
        SetSyncActionScript(NPC_9, A0988_SMITHY_COMPONENT),
        JmpToSubroutine(["EVENT_3794_set_bit_144"]),
        Pause(10),
        JmpToSubroutine(["EVENT_3794_set_bit_149"]),
        Pause(30),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=6, is_sequence=True, looping=True
                )
            ],
        ),
        JmpToSubroutine(["EVENT_3794_set_bit_144"]),
        Pause(10),
        JmpToSubroutine(["EVENT_3794_set_bit_149"]),
        Pause(30),
        UnfreezeCamera(),
        SetBit(TEMP_7043_5),
        UnsyncActionScript(NPC_9),
        UnsyncActionScript(NPC_4),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASPause(20), ASSetWalkingSpeed(NORMAL), ASWalk1StepNortheast()],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(20),
                ASResetProperties(),
                ASSetWalkingSpeed(FAST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASJumpToHeight(152),
                ASWalkNortheastSteps(2),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNortheastSteps(2),
                ASFloatingOff(),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        Pause(10),
        PauseActionScript(NPC_8),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASWalkNortheastPixels(2),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkSouthPixels(4),
                ASWalkSouthwestPixels(6),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(40),
                ASSetSpriteSequence(
                    index=12, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkNortheastPixels(2),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestPixels(2),
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftZDownPixels(4),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASPause(10),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSouthwestPixels(2),
                ASSetWalkingSpeed(SLOW),
                ASWalkNortheastPixels(2),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkNortheastPixels(1),
                ASWalkNorthPixels(2),
                ASSetSpriteSequence(
                    index=4, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(55),
        InitiateBattleMask(),
        EnterArea(
            room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
            face_direction=NORTHEAST,
            x=4,
            y=51,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
        SetBit(TEMP_7043_1, identifier="EVENT_3794_set_bit_144"),
        UnsyncActionScript(NPC_8),
        ClearBit(TEMP_7043_1),
        SetSyncActionScript(NPC_8, A0242_SMITHY_COMPONENT),
        Return(),
        SetBit(TEMP_7043_1, identifier="EVENT_3794_set_bit_149"),
        ClearBit(TEMP_7043_3),
        UnsyncActionScript(NPC_8),
        ClearBit(TEMP_7043_1),
        SetSyncActionScript(NPC_8, A0987_SMITHY_COMPONENT),
        Return(),
    ]
)
