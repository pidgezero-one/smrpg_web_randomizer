# pylint: disable=C0301

"""E3616_NIMBUS_INN_LOADER_FROM_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_7, ["EVENT_3616_stop_sound_1"]),
        FadeInFromBlack(sync=False),
        Return(),
        StopSound(identifier="EVENT_3616_stop_sound_1"),
        FadeOutMusicToVolume(duration=1, volume=96),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3616_ret_26"]),
        RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3616_ret_26"),
    ]
)
