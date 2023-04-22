"""A0226_ENDING_CUTSCENE_EFFECT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [BPL262728(), FloatingOff(), SetObjectMemoryBits(arg_1=0x0E, bits=[3]), Return()]
)
