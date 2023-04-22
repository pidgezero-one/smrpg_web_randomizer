# pylint: disable=C0301

"""E0169_MIMIC_1_GRANT_STAR_PIECE_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [SetVarToConst(PRIMARY_TEMP_7000, 512), JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE)]
)
