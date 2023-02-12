# E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        JmpToEvent(E3098_PROGRESSIVE_EGG_NPC_GRANT),
    ]
)
