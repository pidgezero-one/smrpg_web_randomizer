# pylint: disable=C0301

"""E1323_TOWER_LOBBY_HENCHMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E1602_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_DO_NOT_REMOVE_FROM_LEVEL
        ),
        RunDialog(
            dialog_id=DI2560_TOWER_HENCHMAN_1,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Pause(5),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        JmpIfBitClear(GAME_OVER, ["EVENT_1323_remove_from_current_level_5"]),
        ResetAndChooseGame(),
        RemoveObjectFromCurrentLevel(
            NPC_4, identifier="EVENT_1323_remove_from_current_level_5"
        ),
        RemoveObjectFromSpecificLevel(NPC_4, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
