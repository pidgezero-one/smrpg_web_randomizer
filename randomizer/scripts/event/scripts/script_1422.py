# pylint: disable=C0301

"""E1422_RESCUE_TOAD_MUSHROOM_WAY_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        DisableObjectTrigger(NPC_7),
        PauseActionScript(NPC_7),
        PauseActionScript(NPC_8),
        StartBattleAtBattlefield(4, BF09_GRASSLANDS),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1422_set_action_script_async_7"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_1422_reset_and_choose_game_37"]),
        Jmp(["EVENT_1422_freeze_all_npcs_until_return_15"]),
        SetAsyncActionScript(
            NPC_7, A0015_DO_NOTHING, identifier="EVENT_1422_set_action_script_async_7"
        ),
        SetAsyncActionScript(NPC_8, A0015_DO_NOTHING),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASBPL262728(),
                ASTransferToXYZF(x=13, y=28, z=12, direction=EAST),
                ASFaceSoutheast(),
                ASReturn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASBPL262728(),
                ASTransferToXYZF(x=13, y=28, z=14, direction=EAST),
                ASFaceSoutheast(),
                ASReturn(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=14, y=28, z=6, direction=EAST),
                ASFaceSouth(),
                ASReturn(),
            ],
        ),
        RunBackgroundEvent(
            event_id=E1432_RESCUE_TOAD_EXTENDED, return_on_level_exit=True
        ),
        FadeInFromBlack(sync=False),
        Return(),
        FreezeAllNPCsUntilReturn(
            identifier="EVENT_1422_freeze_all_npcs_until_return_15"
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASFloatingOn(),
                ASBPL262728(),
                ASSetPriority(3),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASTransferToXYZF(x=14, y=28, z=6, direction=EAST),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(NORMAL),
                ASSequenceLoopingOn(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=13, y=29, z=6, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromSpecificLevel(NPC_8, R204_MUSHROOM_WAY_AREA_02),
        FadeInFromBlack(sync=False),
        Pause(15),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Pause(15),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetAllSpeeds(FASTER),
                ASWalkSoutheastSteps(3),
                ASJumpToHeight(112),
                ASWalkSoutheastSteps(11),
                ASVisibilityOff(),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(NPC_7, R204_MUSHROOM_WAY_AREA_02),
        SummonObjectToSpecificLevel(NPC_5, R205_MUSHROOM_WAY_AREA_03),
        SetBit(TOAD_IN_MUSHROOM_WAY_2),
        UnfreezeAllNPCs(),
        Return(),
        ResetAndChooseGame(identifier="EVENT_1422_reset_and_choose_game_37"),
        Return(),
    ]
)
