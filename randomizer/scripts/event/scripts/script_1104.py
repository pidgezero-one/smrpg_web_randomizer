# pylint: disable=C0301

"""E1104_TADPOLE_POND_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DeactivateSoundChannels([]),
        ActionQueueAsync(target=NPC_9, subscript=[ASWalkSouthwestPixels(1)]),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1104_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1104_ret_26"]),
        RunEventAsSubroutine(E3893_TADPOLE_POND_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1104_ret_26"),
    ]
)
