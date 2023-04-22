"""A0672_ROSE_TOWN_LIBERATED_WATER_KID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpToSubroutine(["ACTION_672_visibility_off_10"]),
        WalkSouthwestSteps(1),
        WalkNorthwestSteps(1),
        FaceSoutheast(),
        SequenceLoopingOff(),
        Pause(160),
        WalkSoutheastSteps(1),
        WalkNortheastSteps(1),
        JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
        Return(),
        VisibilityOff(identifier="ACTION_672_visibility_off_10"),
        TransferToXYZF(x=15, y=55, z=2, direction=EAST),
        FaceSoutheast(),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FAST),
        VisibilityOn(),
        Walk1StepSoutheast(),
        SetSolidityBits(cant_walk_through=True),
        WalkSoutheastSteps(4),
        SetSolidityBits(cant_pass_walls=True),
        FloatingOn(),
        WalkSouthwestSteps(2),
        ClearSolidityBits(cant_pass_walls=True),
        FloatingOff(),
        WalkSouthwestSteps(2),
        Return(),
        WalkNortheastSteps(2, identifier="ACTION_672_shift_northeast_steps_26"),
        WalkNortheastPixels(8),
        SetSolidityBits(cant_pass_walls=True),
        FloatingOn(),
        WalkNortheastSteps(1),
        ClearSolidityBits(cant_pass_walls=True),
        FloatingOff(),
        WalkNortheastPixels(8),
        WalkNorthwestSteps(4),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Walk1StepNorthwest(),
        VisibilityOff(),
        TransferToXYZF(x=16, y=85, z=0, direction=EAST),
        Return(),
    ]
)
