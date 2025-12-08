# pylint: disable=C0301

"""E0650_MARRYMORE_SANCTUARY_CANDLE_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            mod_id=5),
        PlaySound(sound=SO084_SMOKED, channel=6),
        Dec(TEMP_70AE),
        SetVarToConst(TIMER_701C, 240),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E0651_MARRYMORE_SANCTUARY_CANDLE_5, timer_var=TIMER_701C
        ),
        Return(),
    ]
)
