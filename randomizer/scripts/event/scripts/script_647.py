# pylint: disable=C0301

"""E0647_MARRYMORE_SANCTUARY_CANDLE_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            mod_id=0,
        ),
        PlaySound(sound=SO084_SMOKED, channel=6),
        Dec(TEMP_70AE),
        SetVarToConst(TIMER_701E, 300),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E0648_MARRYMORE_SANCTUARY_CANDLE_2, timer_var=TIMER_701E
        ),
        Return(),
    ]
)
