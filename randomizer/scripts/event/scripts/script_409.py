# pylint: disable=C0301

"""E0409_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_2F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0771_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_2F_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        JmpIfBitSet(
            OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED,
            ["EVENT_409_jmp_if_object_not_in_level_4"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ["EVENT_261_1"],
            identifier="EVENT_409_jmp_if_object_not_in_level_4",
        ),
        SummonObjectToCurrentLevel(NPC_2),
        PauseActionScript(NPC_2),
        SetSyncActionScript(NPC_2, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
