"""A0889_JAWFUL_EXTENDED_HITBOXES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Pause(60),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        Return(),
    ]
)
