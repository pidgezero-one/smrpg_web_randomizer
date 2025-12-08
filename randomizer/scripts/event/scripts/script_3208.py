# pylint: disable=C0301

"""E3208_WATER_WHIRLPOOL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO112_DRAINING_WATER, channel=4),
                ASDb(bytearray(b"\xc8\x90")),
                ASRunAwayShift(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASObjectMemoryModifyBits(arg_1=0x0C, set_bits=[4], clear_bits=[3, 5]),
                ASFloatingOff(),
                ASStartLoopNTimes(39),
                ASTurnClockwise45DegreesNTimes(1),
                ASShiftZDownPixels(2),
                ASEndLoop(),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_walls=True),
            ]),
        Return(),
    ]
)
