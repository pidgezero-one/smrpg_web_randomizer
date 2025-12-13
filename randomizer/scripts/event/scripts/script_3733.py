# pylint: disable=C0301

"""E3733_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToBackgroundThread2(),
        JmpIfBitSet(NIMBUS_PLATFORM_ACTIVE, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3584_ret_0"]),
        SetBit(TEMP_7043_1),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        Set7000ToTappedButton(identifier="EVENT_3733_set_7000_to_tapped_button_5"),
        JmpIfBitClear(TEMP_7043_1, ["EVENT_3584_ret_0"]),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3733_jmp_if_present_in_current_level_11"]
        ),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_3584_ret_0"]),
        Pause(1),
        Jmp(["EVENT_3733_set_7000_to_tapped_button_5"]),
        JmpIfObjectInCurrentLevel(
            NPC_6,
            ["EVENT_3733_play_sound_13"],
            identifier="EVENT_3733_jmp_if_present_in_current_level_11"),
        Jmp(["EVENT_3733_summon_to_current_level_15"]),
        PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3733_play_sound_13"),
        SetBit(NIMBUS_PLATFORM_ACTIVE),
        SummonObjectToCurrentLevel(
            NPC_6, identifier="EVENT_3733_summon_to_current_level_15"
        ),
        Return(),
    ]
)
