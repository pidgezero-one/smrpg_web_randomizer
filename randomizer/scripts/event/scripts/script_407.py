# pylint: disable=C0301

"""E0407_COUNTERTOP_SHYSTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_704A_2),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            ["EVENT_405_pause_action_script_6"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
