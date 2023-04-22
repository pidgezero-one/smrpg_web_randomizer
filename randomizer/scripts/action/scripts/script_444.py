"""A0444_SHIP_HIDDEN_CHEST_BLOCK_TRIGGER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript([ObjectMemorySetBit(arg_1=0x0D, bits=[6]), Return()])
