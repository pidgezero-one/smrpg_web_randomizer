"""A0119_SLOW_SEQUENCE_LOOP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript([SetSequenceSpeed(SLOW), SequenceLoopingOn(), Return()])
