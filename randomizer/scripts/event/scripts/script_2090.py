# pylint: disable=C0301

"""E2090_MONSTRO_ENTRANCE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(2),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASWalkNorthwestPixels(8),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASWalkNortheastPixels(6), ASFaceSouthwest(), ASPause(1)]),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2090_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2090_ret_26"]),
        RunEventAsSubroutine(E3909_MONSTRO_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2090_ret_26"),
    ]
)
