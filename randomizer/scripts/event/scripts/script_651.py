# pylint: disable=C0301

"""E0651_MARRYMORE_SANCTUARY_CANDLE_5"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            mod_id=2,
        ),
        PlaySound(sound=SO084_SMOKED, channel=6),
        Dec(TEMP_70AE),
        SetVarToConst(TIMER_701E, 120),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E0652_MARRYMORE_SANCTUARY_CANDLE_6, timer_var=TIMER_701E
        ),
        Return(),
    ]
)
