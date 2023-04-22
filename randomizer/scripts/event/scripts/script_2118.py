# pylint: disable=C0301

"""E2118_INITIATE_STATUE_POLISHER_MANUAL_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        SetVarToConst(PRIMARY_TEMP_7000, 520),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        JmpIfBitClear(GAME_OVER, ["EVENT_2118_remove_from_level_4"]),
        ResetAndChooseGame(),
        RemoveObjectFromSpecificLevel(
            NPC_2,
            R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            identifier="EVENT_2118_remove_from_level_4",
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        FadeInFromBlack(sync=False),
        ClearBit(STATUE_KEEPER_FIGHT_PRESENT),
        JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_2118_ret_10"]),
        SetBit(STATUE_KEEPER_STAR_PIECE),
        SetVarToConst(PRIMARY_TEMP_7000, 520),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Return(identifier="EVENT_2118_ret_10"),
    ]
)
