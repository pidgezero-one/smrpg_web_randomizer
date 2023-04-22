"""A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [FloatingOff(), SetPriority(3), WalkSoutheastPixels(8), FaceSouthwest(), Return()]
)
