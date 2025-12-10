# pylint: disable=C0301

"""E3413_MINES_SHYGUY_COLLIDE_WITH_BOXES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_3413_jmp_if_bit_set_14_"),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3413_set_7010_to_object_xyz_13"]),
        Jmp(["EVENT_3413_jmp_if_bit_set_14_"]),
        Set70107015ToObjectXYZ(
            NPC_0, identifier="EVENT_3413_set_7010_to_object_xyz_13"
        ),
        JmpToEvent(E3412_EMPTY),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASFixedFCoordOn(),
                ASTransferToObjectXY(NPC_0),
                ASSetSequenceSpeed(FAST),
                ASJumpToHeight(height=80, silent=True),
                ASShiftSouthSteps(2),
                ASJumpToHeight(height=32, silent=True),
                ASWalkSouthPixels(3),
                ASJumpToHeight(height=8, silent=True),
                ASWalkSouthPixels(1),
                ASPause(20),
                ASSetSolidityBits(cant_jump_through=True),
            ],
            identifier="EVENT_3413_action_queue_sync_15"),
        ClearBit(TEMP_7043_0),
        Return(identifier="EVENT_3413_r"),
    ]
)
