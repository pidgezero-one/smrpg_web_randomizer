# pylint: disable=C0301

"""E3338_VOLCANO_TRAMPOLINE_TO_2ND_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_3338_open_location_182"]),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        StopMusicFDA2(),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        SetVarToConst(TEMP_7026, 0),
        SetVarToConst(TEMP_7028, 0),
        SetVarToConst(TEMP_702A, 0),
        SetVarToConst(TEMP_702C, 0),
        JmpIfBitSet(GAME_OVER, ["EVENT_3338_reset_and_choose_game_186"]),
        SetBit(VOLCANO_LIBERATED),
        RestoreAllHP(),
        RestoreAllFP(),
        RunEventAsSubroutine(E0208_UNLOCK_KEEP_IF_GATED_BY_VOLCANO_BOSS),
        SetBit(RETURN_TO_OVERWORLD_AFTER_VOLCANO_STAR_PIECE),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        ExitToWorldMap(
            area=OW50_BARREL_VOLCANO,
            bit_6=True,
            bit_7=True,
            identifier="EVENT_3338_open_location_182"),
        Return(),
        ResetAndChooseGame(identifier="EVENT_3338_reset_and_choose_game_186"),
    ]
)
