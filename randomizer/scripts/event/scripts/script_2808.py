# pylint: disable=C0301

"""E2808_MUSHROOM_WAY_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            TOAD_IN_MUSHROOM_WAY_3,
            ["EVENT_2808_ret_34"],
            identifier="EVENT_2808_jmp_if_bit_set_0"),
        FreezeAllNPCsUntilReturn(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FAST),
                ASWalkToXYCoords(x=27, y=94),
                ASFaceNortheast(),
            ]),
        StopEmbeddedActionScript(MARIO),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2808_restore_all_hp_7"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2808_restore_all_hp_7"),
        RestoreAllFP(),
        SetBit(TOAD_IN_MUSHROOM_WAY_3),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_7),
        SummonObjectToCurrentLevel(NPC_8),
        FreezeAllNPCsUntilReturn(),
        RemoveObjectFromSpecificLevel(NPC_7, R205_MUSHROOM_WAY_AREA_03),
        RemoveObjectFromSpecificLevel(NPC_5, R205_MUSHROOM_WAY_AREA_03),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_5),
        FadeInFromBlack(sync=False),
        UnfreezeCamera(),
        UnfreezeAllNPCs(),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        SetVarToConst(OLD_STAR_PIECE_ID, 200),
        RunEventAsSubroutine(E0186_PARTY_JOIN_LOGIC),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        JmpToEvent(E0199_UNLOCK_BANDITS_IF_GATED_BY_MUSHROOM_WAY),
        Return(identifier="EVENT_2808_ret_34"),
    ]
)
