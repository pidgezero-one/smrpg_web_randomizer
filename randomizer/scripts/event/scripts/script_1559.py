# pylint: disable=C0301

"""E1559_LANDS_END_SPINNY_FLOWER_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [SetVarToConst(X_COORD_2, 1574), JmpToEvent(E1537_SPINNING_FLOWER_CORE_LOGIC)]
)
