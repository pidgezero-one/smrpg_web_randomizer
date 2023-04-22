# pylint: disable=C0301

"""E1627_DYNA_HOUSE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=1, volume=96),
        JmpIfBitClear(MINECART_CLEARED, ["EVENT_1627_jmp_if_bit_clear_14"]),
        JmpIfBitClear(TEMP_7042_1, ["EVENT_1627_summon_to_current_level_7"]),
        SummonObjectToCurrentLevel(NPC_1),
        SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
        SummonObjectToCurrentLevel(
            NPC_2, identifier="EVENT_1627_summon_to_current_level_7"
        ),
        SetSyncActionScript(NPC_2, A0160_SEQUENCE_LOOPING_ON),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfBitClear(
            MINES_BOSS_2_DEFEATED,
            ["EVENT_1627_fade_in_from_black_async_17"],
            identifier="EVENT_1627_jmp_if_bit_clear_14",
        ),
        SummonObjectToCurrentLevel(NPC_1),
        SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
        FadeInFromBlack(
            sync=False, identifier="EVENT_1627_fade_in_from_black_async_17"
        ),
        Return(),
    ]
)
