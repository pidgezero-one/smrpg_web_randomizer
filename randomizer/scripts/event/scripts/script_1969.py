# pylint: disable=C0301

"""E1969_CHECK_IF_STAR_PIECES_FOR_FACTORY_BOSS_COLLECTED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=EXP_STAR_70D5, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 6),
        Return(),
    ]
)
