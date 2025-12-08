# pylint: disable=C0301

"""E2814_MUSHROOM_WAY_3_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR),
        ClearBit(EXP_STAR_BIT_1),
        ClearBit(EXP_STAR_BIT_2),
        ClearBit(EXP_STAR_BIT_3),
        ClearBit(EXP_STAR_BIT_4),
        SetVarToConst(COIN_COUNTER_1, 0),
        SetVarToConst(COIN_COUNTER_2, 0),
        SetVarToConst(COIN_COUNTER_3, 0),
        SetVarToConst(COIN_COUNTER_4, 0),
        SetVarToConst(COIN_COUNTER_5, 0),
        SetVarToConst(COIN_COUNTER_6, 0),
        RemoveObjectFromSpecificLevel(NPC_0, R205_MUSHROOM_WAY_AREA_03),
        RemoveObjectFromSpecificLevel(NPC_1, R205_MUSHROOM_WAY_AREA_03),
        RemoveObjectFromSpecificLevel(NPC_2, R205_MUSHROOM_WAY_AREA_03),
        RunEventAsSubroutine(E0755_MUSHROOM_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2814_run_background_event_13"]
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2814_run_background_event_13"]),
        RunEventAsSubroutine(E3888_MUSHROOM_WAY_STAR_PIECE_SIGNAL),
        RunBackgroundEvent(
            event_id=E2813_MUSHROOM_WAY_3_SUMMON_SPINYS,
            return_on_level_exit=True,
            identifier="EVENT_2814_run_background_event_13"),
        RunBackgroundEvent(
            event_id=E2809_MUSHROOM_WAY_BOSS_THREATENS_YOU,
            return_on_level_exit=True,
            bit_6=True),
        Return(),
    ]
)
