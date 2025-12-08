# pylint: disable=C0301

"""E0265_OCCUPIED_MK_INN_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopSound(),
        FadeOutMusicToVolume(duration=1, volume=96),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_265_run_event_as_subroutine_6"]),
        FadeInFromBlack(sync=False),
        Return(),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_265_run_event_as_subroutine_6"),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_265_ret_26"]),
        RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_265_ret_26"),
    ]
)
