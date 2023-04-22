# pylint: disable=C0301

"""E2802_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2802_pause_0"),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_2802_pause_0"]),
        Set7000ToTappedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_2802_set_7000_to_70A0_short_mem_5"]
        ),
        Jmp(["EVENT_2802_pause_0"]),
        CopyVarToVar(
            from_var=TEMP_70AE,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_2802_set_7000_to_70A0_short_mem_5",
        ),
        CompareVarToConst(PRIMARY_TEMP_7000, 2),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2802_jmp_if_bit_clear_14"]),
        Inc(TEMP_70AE),
        JmpIfBitClear(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_2802_pause_11"]),
        PlaySound(sound=SO014_FLOWER, channel=6),
        Pause(1, identifier="EVENT_2802_pause_11"),
        JmpIfMarioInAir(["EVENT_2802_pause_11"]),
        Jmp(["EVENT_2802_pause_0"]),
        JmpIfBitClear(
            KNIFE_GUY_PRIZE_GRANTED,
            ["EVENT_2802_summon_to_level_16"],
            identifier="EVENT_2802_jmp_if_bit_clear_14",
        ),
        PlaySound(sound=SO014_FLOWER, channel=6),
        SummonObjectToSpecificLevel(
            NPC_4,
            R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO,
            identifier="EVENT_2802_summon_to_level_16",
        ),
        SummonObjectToCurrentLevel(NPC_4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO,
            mod_id=0,
        ),
        Return(),
    ]
)
