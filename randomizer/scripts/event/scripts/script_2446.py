# pylint: disable=C0301

"""E2446_FOREST_BOSS_HENCHMEN_BOUNCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySoundBalance(
            sound=SO077_EXOTIC_BIRD_CALLS,
            balance=56,
            identifier="EVENT_2446_play_sound_balance_0",
        ),
        Pause(24),
        Jmp(["EVENT_2446_play_sound_balance_0"]),
    ]
)
