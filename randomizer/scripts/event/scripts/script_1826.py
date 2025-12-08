# pylint: disable=C0301

"""E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ROSE_WAY_7038, 4224),
        SetVarToConst(ROSE_WAY_703A, 14720),
        SetVarToConst(ROSE_WAY_703C, 512),
        RunBackgroundEvent(
            event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True
        ),
        RunBackgroundEvent(
            event_id=E1831_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_1,
            return_on_level_exit=True,
            bit_6=True),
        RunBackgroundEvent(
            event_id=E1832_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_2,
            return_on_level_exit=True,
            bit_7=True),
        PrioritySet(
            mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
            subscreen=[],
            colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, HALF_INTENSITY]),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1826_play_sound_10"]),
        ClearBit(TEMP_7095_4),
        PlaySound(
            sound=SO011_WHOOSH_AWAY, channel=6, identifier="EVENT_1826_play_sound_10"
        ),
        SetSyncActionScript(NPC_1, A0822_KEEP_JUMPING_TERRAPIN_INIT),
        SetSyncActionScript(NPC_2, A0822_KEEP_JUMPING_TERRAPIN_INIT),
        SetSyncActionScript(NPC_3, A0822_KEEP_JUMPING_TERRAPIN_INIT),
        JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES),
    ]
)
