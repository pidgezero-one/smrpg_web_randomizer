# pylint: disable=C0301,C0103

"""referenced by battle_events BE0015_CROCO_STEALS_ITEMS_YOU_WANT_THEM_BACK, battle_events BE0002_BELOME_SWALLOWS_MALLOW"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=10,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=104,
            y=176,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
    ])
