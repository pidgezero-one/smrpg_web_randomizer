# pylint: disable=C0301

"""E3938_FREESTANDING_CROWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPause(30),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ]),
        JmpToEvent(E3934_GET_CROWN),
    ]
)
