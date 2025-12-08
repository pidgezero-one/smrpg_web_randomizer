# pylint: disable=C0301

"""E1590_SEWER_PIPE_TO_LANDS_END_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFixedFCoordOn(),
                ASWalkNorthwestPixels(8),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFixedFCoordOn(),
                ASWalkNorthwestPixels(8),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        JmpIfBitClear(
            LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_1590_fade_in_from_black_async_4"]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=24, y=30, z=0, direction=EAST),
                ASSetWalkingSpeed(FASTEST),
                ASWalkEastPixels(46),
                ASFaceSouthwest(),
            ]),
        FadeInFromBlack(sync=False, identifier="EVENT_1590_fade_in_from_black_async_4"),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1590_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1590_ret_26"]),
        RunEventAsSubroutine(E3907_LANDS_END_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1590_ret_26"),
    ]
)
