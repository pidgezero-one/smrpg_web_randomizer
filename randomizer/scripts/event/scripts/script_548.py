# pylint: disable=C0301

"""E0548_ROSE_TOWN_OCCUPIED_ARROW_ANIMATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_2, ["EVENT_548_jmp_if_random_above_128_35"]),
        JmpIfBitSet(TEMP_7044_1, ["EVENT_548_jmp_if_random_above_128_39"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_548_jmp_if_random_above_66_19"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_548_jmp_if_random_above_128_13"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_548_jmp_if_random_above_66_23"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_548_jmp_if_random_above_128_17"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4, ["EVENT_548_jmp_if_random_above_66_27"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 5, ["EVENT_548_jmp_if_random_above_128_15"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 6, ["EVENT_548_jmp_if_random_above_66_31"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 7, ["EVENT_548_jmp_if_random_above_128_11"]
        ),
        JmpIfRandom1of2(
            ["EVENT_548_jmp_if_random_above_66_19"],
            identifier="EVENT_548_jmp_if_random_above_128_11",
        ),
        Jmp(["EVENT_548_jmp_if_random_above_66_31"]),
        JmpIfRandom1of2(
            ["EVENT_548_jmp_if_random_above_66_19"],
            identifier="EVENT_548_jmp_if_random_above_128_13",
        ),
        Jmp(["EVENT_548_jmp_if_random_above_66_23"]),
        JmpIfRandom1of2(
            ["EVENT_548_jmp_if_random_above_66_27"],
            identifier="EVENT_548_jmp_if_random_above_128_15",
        ),
        Jmp(["EVENT_548_jmp_if_random_above_66_31"]),
        JmpIfRandom1of2(
            ["EVENT_548_jmp_if_random_above_66_27"],
            identifier="EVENT_548_jmp_if_random_above_128_17",
        ),
        Jmp(["EVENT_548_jmp_if_random_above_66_23"]),
        JmpIfRandom2of3(
            [
                "EVENT_548_jmp_if_random_above_66_23",
                "EVENT_548_jmp_if_random_above_66_31",
            ],
            identifier="EVENT_548_jmp_if_random_above_66_19",
        ),
        SetBit(TEMP_7043_3),
        SetSyncActionScript(NPC_8, A0635_ROSE_TOWN_ARROW),
        Return(),
        JmpIfRandom2of3(
            [
                "EVENT_548_jmp_if_random_above_66_27",
                "EVENT_548_jmp_if_random_above_66_19",
            ],
            identifier="EVENT_548_jmp_if_random_above_66_23",
        ),
        SetBit(TEMP_7043_4),
        SetSyncActionScript(NPC_8, A0635_ROSE_TOWN_ARROW),
        Return(),
        JmpIfRandom2of3(
            [
                "EVENT_548_jmp_if_random_above_66_23",
                "EVENT_548_jmp_if_random_above_66_31",
            ],
            identifier="EVENT_548_jmp_if_random_above_66_27",
        ),
        SetBit(TEMP_7043_5),
        SetSyncActionScript(NPC_8, A0635_ROSE_TOWN_ARROW),
        Return(),
        JmpIfRandom2of3(
            [
                "EVENT_548_jmp_if_random_above_66_27",
                "EVENT_548_jmp_if_random_above_66_19",
            ],
            identifier="EVENT_548_jmp_if_random_above_66_31",
        ),
        SetBit(TEMP_7043_6),
        SetSyncActionScript(NPC_8, A0635_ROSE_TOWN_ARROW),
        Return(),
        JmpIfRandom1of2(
            ["EVENT_548_pause_43"], identifier="EVENT_548_jmp_if_random_above_128_35"
        ),
        SetBit(TEMP_7043_7),
        SetSyncActionScript(NPC_8, A0635_ROSE_TOWN_ARROW),
        Return(),
        JmpIfRandom1of2(
            ["EVENT_548_pause_43"], identifier="EVENT_548_jmp_if_random_above_128_39"
        ),
        SetBit(TEMP_7044_1),
        SetSyncActionScript(NPC_8, A0635_ROSE_TOWN_ARROW),
        Return(),
        Pause(30, identifier="EVENT_548_pause_43"),
        SetBit(TEMP_7044_5),
        Return(),
    ]
)
