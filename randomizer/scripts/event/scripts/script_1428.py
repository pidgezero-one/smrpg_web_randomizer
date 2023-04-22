# pylint: disable=C0301

"""E1428_RESCUE_TOAD_MUSHROOM_WAY_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E1602_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_DO_NOT_REMOVE_FROM_LEVEL
        ),
        DisableObjectTrigger(NPC_8),
        DisableObjectTrigger(NPC_9),
        FreezeAllNPCsUntilReturn(),
        StartBattleAtBattlefield(6, BF09_GRASSLANDS),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1428_enable_trigger_21"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_1428_reset_and_choose_game_27"]),
        RemoveObjectFromSpecificLevel(NPC_9, R203_MUSHROOM_WAY_AREA_01),
        RemoveObjectFromCurrentLevel(NPC_9),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASTransferToXYZF(x=10, y=22, z=0, direction=EAST),
                ASFaceSoutheast(),
                ASSequenceLoopingOn(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=10, y=23, z=0, direction=EAST),
                ASFaceNorthwest(),
            ],
        ),
        SetBit(TOAD_IN_MUSHROOM_WAY_1),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetAllSpeeds(FASTER),
                ASWalkNortheastSteps(4),
                ASWalkNorthwestSteps(3),
                ASWalkNortheastSteps(4),
                ASVisibilityOff(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromSpecificLevel(NPC_8, R203_MUSHROOM_WAY_AREA_01),
        UnfreezeAllNPCs(),
        Return(),
        EnableObjectTrigger(NPC_8, identifier="EVENT_1428_enable_trigger_21"),
        EnableObjectTrigger(NPC_9),
        SetTempSyncActionScript(NPC_8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        SetSyncActionScript(NPC_9, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False),
        Return(),
        ResetAndChooseGame(identifier="EVENT_1428_reset_and_choose_game_27"),
        Return(),
    ]
)
