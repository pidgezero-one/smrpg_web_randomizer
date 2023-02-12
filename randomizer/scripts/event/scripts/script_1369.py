# E1369_CURTAIN_GAME_SUCCESS_FAILURE_FIGHT_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(30, identifier="EVENT_1369_pause_0"),
        EnableControlsUntilReturn([]),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_1369_action_queue_sync_5"]),
        ResetAndChooseGame(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
                ASTransferToXYZF(x=3, y=23, z=0, direction=EAST),
                ASShiftSoutheastPixels(8),
                ASFaceNortheast(),
            ],
            identifier="EVENT_1369_action_queue_sync_5",
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASTransferToXYZF(x=4, y=21, z=0, direction=EAST),
                ASShiftSoutheastPixels(8),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(FAST),
                ASTransferToXYZF(x=5, y=20, z=0, direction=EAST),
                ASShiftSoutheastPixels(8),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(FAST),
                ASTransferToXYZF(x=5, y=19, z=0, direction=EAST),
                ASShiftSoutheastPixels(8),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(FAST),
                ASTransferToXYZF(x=6, y=18, z=0, direction=EAST),
                ASShiftSoutheastPixels(8),
                ASFaceSouthwest(),
            ],
        ),
        UnfreezeCamera(),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=2,
        ),
        SetBit(TOWER_BOSS_1_DEFEATED),
        FadeInFromBlack(sync=False),
        ActionQueueSync(target=NPC_0, subscript=[ASShiftSouthwestSteps(4)]),
        ActionQueueSync(target=NPC_1, subscript=[ASShiftSouthwestSteps(4)]),
        ActionQueueSync(target=NPC_2, subscript=[ASShiftSouthwestSteps(4)]),
        ActionQueueSync(target=NPC_3, subscript=[ASShiftSouthwestSteps(4)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(96),
                ASShiftNorthwestSteps(2),
                ASSetPriority(2),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSetWalkingSpeed(NORMAL),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0, subscript=[ASShiftSouthwestSteps(1), ASVisibilityOff()]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASShiftSouthwestSteps(2), ASVisibilityOff()]
        ),
        ActionQueueSync(
            target=NPC_2, subscript=[ASShiftSouthwestSteps(3), ASVisibilityOff()]
        ),
        ActionQueueAsync(
            target=NPC_3, subscript=[ASShiftSouthwestSteps(4), ASVisibilityOff()]
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        Pause(30),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        RestoreAllHP(),
        RestoreAllFP(),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
