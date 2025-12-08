# pylint: disable=C0301

"""E2429_FOREST_UNKNOWN_SUMMONER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_5, ["EVENT_2429_ret_47"]),
        SetBit(TEMP_7044_5),
        JmpIfRandom2of3(
            ["EVENT_2429_remove_from_level_6", "EVENT_2429_remove_from_level_9"]
        ),
        SummonObjectToSpecificLevel(
            NPC_0, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        Jmp(["EVENT_2429_jmp_if_random_above_66_11"]),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER,
            identifier="EVENT_2429_remove_from_level_6"),
        SummonObjectToSpecificLevel(
            NPC_2, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        Jmp(["EVENT_2429_jmp_if_random_above_66_11"]),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER,
            identifier="EVENT_2429_remove_from_level_9"),
        RemoveObjectFromSpecificLevel(
            NPC_2, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        JmpIfRandom2of3(
            ["EVENT_2429_remove_from_level_15", "EVENT_2429_remove_from_level_18"],
            identifier="EVENT_2429_jmp_if_random_above_66_11"),
        SummonObjectToSpecificLevel(
            NPC_1, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        Jmp(["EVENT_2429_jmp_if_random_above_66_20"]),
        RemoveObjectFromSpecificLevel(
            NPC_1,
            R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER,
            identifier="EVENT_2429_remove_from_level_15"),
        SummonObjectToSpecificLevel(
            NPC_3, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        Jmp(["EVENT_2429_jmp_if_random_above_66_20"]),
        RemoveObjectFromSpecificLevel(
            NPC_1,
            R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER,
            identifier="EVENT_2429_remove_from_level_18"),
        RemoveObjectFromSpecificLevel(
            NPC_3, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER
        ),
        JmpIfRandom2of3(
            ["EVENT_2429_remove_from_level_24", "EVENT_2429_remove_from_level_27"],
            identifier="EVENT_2429_jmp_if_random_above_66_20"),
        SummonObjectToSpecificLevel(NPC_0, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        RemoveObjectFromSpecificLevel(NPC_3, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Jmp(["EVENT_2429_jmp_if_random_above_66_29"]),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            identifier="EVENT_2429_remove_from_level_24"),
        SummonObjectToSpecificLevel(NPC_3, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Jmp(["EVENT_2429_jmp_if_random_above_66_29"]),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            identifier="EVENT_2429_remove_from_level_27"),
        RemoveObjectFromSpecificLevel(NPC_3, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        JmpIfRandom2of3(
            ["EVENT_2429_remove_from_level_33", "EVENT_2429_remove_from_level_36"],
            identifier="EVENT_2429_jmp_if_random_above_66_29"),
        SummonObjectToSpecificLevel(NPC_1, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        RemoveObjectFromSpecificLevel(NPC_4, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Jmp(["EVENT_2429_jmp_if_random_above_66_38"]),
        RemoveObjectFromSpecificLevel(
            NPC_1,
            R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            identifier="EVENT_2429_remove_from_level_33"),
        SummonObjectToSpecificLevel(NPC_4, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Jmp(["EVENT_2429_jmp_if_random_above_66_38"]),
        RemoveObjectFromSpecificLevel(
            NPC_1,
            R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            identifier="EVENT_2429_remove_from_level_36"),
        RemoveObjectFromSpecificLevel(NPC_4, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        JmpIfRandom2of3(
            ["EVENT_2429_remove_from_level_42", "EVENT_2429_remove_from_level_45"],
            identifier="EVENT_2429_jmp_if_random_above_66_38"),
        SummonObjectToSpecificLevel(NPC_2, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        RemoveObjectFromSpecificLevel(NPC_5, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Jmp(["EVENT_2429_ret_47"]),
        RemoveObjectFromSpecificLevel(
            NPC_2,
            R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            identifier="EVENT_2429_remove_from_level_42"),
        SummonObjectToSpecificLevel(NPC_5, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Jmp(["EVENT_2429_ret_47"]),
        RemoveObjectFromSpecificLevel(
            NPC_2,
            R235_FOREST_MAZE_AREA_08_UNDERGROUND,
            identifier="EVENT_2429_remove_from_level_45"),
        RemoveObjectFromSpecificLevel(NPC_5, R235_FOREST_MAZE_AREA_08_UNDERGROUND),
        Return(identifier="EVENT_2429_ret_47"),
    ]
)
