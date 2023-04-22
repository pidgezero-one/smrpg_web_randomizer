# pylint: disable=C0301

"""E1346_TOWER_HENCHMAN_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
            ["EVENT_1346_ret_16"],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASTransferToXYZF(x=2, y=106, z=0, direction=EAST),
                ASFaceNorthwest(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASTransferToXYZF(x=1, y=105, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceSoutheast(),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASSetSequenceSpeed(FAST),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSoutheastSteps(3),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSetSequenceSpeed(FAST),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSoutheastSteps(3),
            ],
        ),
        Pause(30),
        RunDialog(
            dialog_id=DI2572_TOWER_HENCHMAN_2,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Pause(5),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        JmpIfBitClear(GAME_OVER, ["EVENT_1346_remove_from_current_level_11"]),
        ResetAndChooseGame(),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_1346_remove_from_current_level_11"
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        FadeInFromBlack(sync=False),
        Return(identifier="EVENT_1346_ret_16"),
    ]
)
