# pylint: disable=C0301

"""E0654_MARRYMORE_SANCTUARY_CANDLE_8"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            mod_id=7),
        PlaySound(sound=SO084_SMOKED, channel=6),
        Dec(TEMP_70AE),
        Return(),
    ]
)
