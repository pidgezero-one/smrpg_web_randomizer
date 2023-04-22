# pylint: disable=C0301

"""E3110_FREESTANDING_JUICE_BAR_CARD_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT),
    ]
)
