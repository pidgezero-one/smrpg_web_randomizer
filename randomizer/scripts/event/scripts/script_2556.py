# pylint: disable=C0301

"""E2556_BEAN_VALLEY_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2556_restore_all_hp_3"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2556_restore_all_hp_3"),
        RestoreAllFP(),
        SetBit(BEAN_VALLEY_BOSS_DEFEATED),
        RemoveObjectFromSpecificLevel(NPC_0, R254_BEAN_VALLEY_SMILAX_AREA),
        RemoveObjectFromSpecificLevel(NPC_1, R254_BEAN_VALLEY_SMILAX_AREA),
        RemoveObjectFromSpecificLevel(NPC_2, R254_BEAN_VALLEY_SMILAX_AREA),
        SummonObjectToSpecificLevel(NPC_3, R254_BEAN_VALLEY_SMILAX_AREA),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASSetSpriteSequence(index=0, is_sequence=True, looping=True)],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASShiftNorthSteps(4)]),
        Pause(16),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSequenceLoopingOff(),
                ASResetProperties(),
                ASPause(32),
                ASSetSpriteSequence(index=2, looping=False),
                ASPause(16),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        Pause(40),
        Pause(24),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASShadowOn(),
                ASWalkNorthwestSteps(16),
            ],
        ),
        SetSyncActionScript(NPC_3, A0689_BEAN_VALLEY_BOSS_PRIZE_DRIFTS_DOWN),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
