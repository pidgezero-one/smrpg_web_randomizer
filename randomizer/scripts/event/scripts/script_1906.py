# E1906_TURN_OFF_MARIO_SHADOW

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [ActionQueueSync(target=MARIO, subscript=[ASShadowOn()]), Return()]
)
