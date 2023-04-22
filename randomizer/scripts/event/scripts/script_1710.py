# pylint: disable=C0301

"""E1710_BANDITS_WAY_5_LOADER_BACKGROUND_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpToSubroutine(["EVENT_1709_enable_controls_until_return_43"]),
        SetSyncActionScript(NPC_1, A0467_BANDITS_WAY_5_TROOPA_CHASE),
        SetSyncActionScript(NPC_2, A0467_BANDITS_WAY_5_TROOPA_CHASE),
        SetSyncActionScript(NPC_3, A0467_BANDITS_WAY_5_TROOPA_CHASE),
        SetSyncActionScript(NPC_4, A0467_BANDITS_WAY_5_TROOPA_CHASE),
        JmpToSubroutine(["EVENT_1709_action_queue_async_55"]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASFaceNorthwest(),
                ASPause(4),
                ASSetWalkingSpeed(VERY_FAST),
                ASStartLoopNTimes(1),
                ASAddZCoord1Step(),
                ASDecZCoord1Step(),
                ASEndLoop(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASStartLoopNTimes(3),
                ASPause(8),
                ASFaceSouthwest(),
                ASPause(5),
                ASFaceSoutheast(),
                ASPause(8),
                ASFaceSouthwest(),
                ASPause(5),
                ASFaceNorthwest(),
                ASEndLoop(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASWalk1StepSouthwest(),
                ASWalkSouthwestPixels(8),
                ASSetSpriteSequence(
                    index=5, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        Pause(60),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASResetProperties(),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASSetPriority(3),
                ASJumpToHeight(108),
                ASWalk1StepNortheast(),
            ],
        ),
        Pause(23),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromSpecificLevel(NPC_8, R206_BANDITS_WAY_AREA_05),
        RestoreAllHP(),
        RestoreAllFP(),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=6, y=88)],
        ),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        Pause(30),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetPriority(3),
                ASVisibilityOn(),
                ASShadowOn(),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_1710_action_queue_async_43_SUBSCRIPT_pause_4"
                ),
                ASJmpIfObjectInAir(
                    NPC_9, ["EVENT_1710_action_queue_async_43_SUBSCRIPT_pause_4"]
                ),
                ASShadowOff(),
                ASSetSolidityBits(cant_walk_through=True),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=6),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkNorthPixels(4),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(4),
            ],
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(5),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=6),
                ASPause(55),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASDb(bytearray(b"\xc8\x80")),
                ASAddConstToVar(X_COORD_2, 65532),
                ASAddConstToVar(Y_COORD_2, 65520),
                ASRunAwayShift(),
                ASSetWalkingSpeed(NORMAL),
                ASJmp(["EVENT_1710_set_bit_47"]),
                ASShiftSouthSteps(6),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        SetBit(MUSHROOM_KINGDOM_OCCUPIED, identifier="EVENT_1710_set_bit_47"),
        SetBit(BANDITS_WAY_LIBERATED),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
