# pylint: disable=C0301

"""E0384_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_ANTECHAMBER_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0769_MUSHROOM_KINGDOM_OCCUPIED_PEACHS_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ["EVENT_384_jmp_if_object_not_in_level_11"]),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=12, y=97, z=4, direction=EAST),
                ASFaceNortheast(),
            ],
            identifier="EVENT_384_action_queue_async_3"),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            mod_id=1),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            ["EVENT_384_fade_in_from_black_async_9"]),
        RemoveObjectFromSpecificLevel(
            NPC_2, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            mod_id=2),
        FadeInFromBlack(sync=False, identifier="EVENT_384_fade_in_from_black_async_9"),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_384_action_queue_async_3"],
            identifier="EVENT_384_jmp_if_object_not_in_level_11"),
        JmpToEvent(E0257_FADE_IN_ASYNC),
    ]
)
