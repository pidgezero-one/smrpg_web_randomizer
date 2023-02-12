# E3726_NIMBUS_CASTLE_ANTECHAMBER_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3726_remove_from_current_level_5"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            ["EVENT_3726_fade_in_from_black_async_3"],
        ),
        ActionQueueAsync(target=NPC_4, subscript=[ASSetPriority(3)]),
        RunEventAsSubroutine(
            E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False, identifier="EVENT_3726_fade_in_from_black_async_3"),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_4, identifier="EVENT_3726_remove_from_current_level_5"
        ),
        SummonObjectToCurrentLevel(NPC_2),
        SummonObjectToCurrentLevel(NPC_3),
        RunEventAsSubroutine(
            E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
