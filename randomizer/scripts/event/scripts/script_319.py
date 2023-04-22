# pylint: disable=C0301

"""E0319_TOADSTOOL_ANTECHAMBER_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [SummonObjectToCurrentLevel(NPC_0), FadeInFromBlack(sync=False), Return()]
)
