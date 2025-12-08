# pylint: disable=C0301

"""E2627_FACTORY_3RD_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["EVENT_2627_ret_47"]
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=7, y=88)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_2627_action_queue_async_3_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2627_action_queue_async_3_SUBSCRIPT_pause_0"]
                ),
                ASWalkToXYCoords(x=11, y=113),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_10, subscript=[ASSetWalkingSpeed(FAST), ASWalkSoutheastSteps(7)]
        ),
        Pause(32),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2627_restore_all_hp_30"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2627_restore_all_hp_30"),
        RestoreAllFP(),
        StopEmbeddedActionScript(NPC_10),
        RemoveObjectFromSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03),
        RemoveObjectFromCurrentLevel(NPC_10),
        FadeInFromBlack(sync=False),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_2627_ret_47"),
    ]
)
