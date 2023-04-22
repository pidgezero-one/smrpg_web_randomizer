# pylint: disable=C0301

"""E0166_FREESTANDING_GRANT_STAR_PIECE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO081_STAR, channel=6),
                ASPause(30),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        JmpToEvent(E3092_STAR_PIECE_GRANT),
    ]
)
