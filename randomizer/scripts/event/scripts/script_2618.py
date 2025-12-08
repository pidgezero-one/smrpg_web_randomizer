# pylint: disable=C0301

"""E2618_FACTORY_2ND_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(INNER_FACTORY_ROOM_3_COMPLETED, ["EVENT_2618_ret_118"]),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=3, y=17)]),
        SetSyncActionScript(NPC_12, A0960_FACTORY_2ND_BOSS_HENCHMAN),
        SetSyncActionScript(NPC_13, A0960_FACTORY_2ND_BOSS_HENCHMAN),
        SetSyncActionScript(NPC_14, A0960_FACTORY_2ND_BOSS_HENCHMAN),
        Pause(16),
        ActionQueueAsync(
            target=MARIO, subscript=[ASPause(16), ASShiftToXYCoords(x=11, y=49)]
        ),
        UnsyncDialog(),
        SetSyncActionScript(NPC_12, A0961_FACTORY_2ND_BOSS_HENCHMAN),
        SetSyncActionScript(NPC_13, A0961_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_14, A0961_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_13, A0960_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_13, A0961_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_12, A0960_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_12, A0961_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_14, A0960_FACTORY_2ND_BOSS_HENCHMAN),
        SetAsyncActionScript(NPC_14, A0961_FACTORY_2ND_BOSS_HENCHMAN),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_15,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(2),
                ASSetSpriteSequence(
                    index=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASWalkNorthwestSteps(2),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FAST),
                ASFaceSoutheast(),
                ASResetProperties(),
                ASSequenceLoopingOn(),
                ASWalkNortheastSteps(2),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FAST),
                ASFaceSoutheast(),
                ASResetProperties(),
                ASSequenceLoopingOn(),
                ASWalkNortheastPixels(6),
                ASWalk1StepSoutheast(),
                ASWalkSoutheastPixels(8),
                ASFaceSouthwest(),
            ]),
        ActionQueueAsync(
            target=NPC_14,
            subscript=[
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FASTER),
                ASFaceSoutheast(),
                ASResetProperties(),
                ASSequenceLoopingOn(),
                ASWalkSoutheastSteps(3),
                ASWalk1StepSouthwest(),
                ASWalkSouthwestPixels(4),
            ]),
        SetSyncActionScript(NPC_12, A0401_SEQUENCE_LOOPING_OFF),
        SetSyncActionScript(NPC_13, A0401_SEQUENCE_LOOPING_OFF),
        SetAsyncActionScript(NPC_14, A0401_SEQUENCE_LOOPING_OFF),
        Pause(32),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkToXYCoords(x=5, y=23)]),
        ActionQueueSync(target=NPC_12, subscript=[ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_13, subscript=[ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_14, subscript=[ASFaceSoutheast()]),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        ActionQueueSync(
            target=NPC_12, subscript=[ASWalk1StepSoutheast(), ASWalkSoutheastPixels(8)]
        ),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASWalk1StepSouthwest(),
                ASWalkSouthwestPixels(8),
                ASFaceSoutheast(),
            ]),
        ActionQueueSync(
            target=NPC_14,
            subscript=[
                ASWalk1StepNortheast(),
                ASWalk1StepNorthwest(),
                ASWalkNorthwestPixels(8),
                ASFaceSoutheast(),
            ]),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASWalk1StepSoutheast(),
                ASWalkSoutheastPixels(8),
                ASSetSpriteSequence(
                    index=2, is_mold=True, is_sequence=True, looping=True
                ),
                ASWalk1StepNortheast(),
                ASWalkNortheastPixels(8),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
            ]),
        ActionQueueSync(
            target=NPC_15, subscript=[ASSetWalkingSpeed(FAST), ASWalk1StepSoutheast()]
        ),
        ActionQueueSync(
            target=NPC_12, subscript=[ASSetWalkingSpeed(FAST), ASWalkSoutheastSteps(4)]
        ),
        ActionQueueSync(
            target=NPC_13, subscript=[ASSetWalkingSpeed(FAST), ASWalkSoutheastSteps(4)]
        ),
        ActionQueueSync(
            target=NPC_14, subscript=[ASSetWalkingSpeed(FAST), ASWalkSoutheastSteps(4)]
        ),
        ActionQueueSync(
            target=NPC_15,
            subscript=[ASSetWalkingSpeed(NORMAL), ASWalkSoutheastSteps(2)]),
        Pause(24),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2618_restore_all_hp_89"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2618_restore_all_hp_89"),
        RestoreAllFP(),
        SetBit(INNER_FACTORY_ROOM_3_COMPLETED),
        RemoveObjectFromCurrentLevel(NPC_12),
        RemoveObjectFromCurrentLevel(NPC_13),
        RemoveObjectFromCurrentLevel(NPC_14),
        RemoveObjectFromCurrentLevel(NPC_15),
        RemoveObjectFromSpecificLevel(NPC_12, R471_FACTORY_GROUNDS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_13, R471_FACTORY_GROUNDS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_14, R471_FACTORY_GROUNDS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_15, R471_FACTORY_GROUNDS_AREA_02),
        FadeInFromBlack(sync=False),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_2618_ret_118"),
    ]
)
