# pylint: disable=C0301

"""E3343_VOLCANO_FINAL_BOSS_PATH_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(VOLCANO_PENULTIMATE_ROOM_ANIMATION_COMPLETED, ["EVENT_3343_ret_8"]),
        SetBit(VOLCANO_PENULTIMATE_ROOM_ANIMATION_COMPLETED),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASDb(bytearray(b"\xfd\xf2")),
                ASWalk1StepSouthwest(),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASDb(bytearray(b"\xfd\xf2")),
                ASWalkSouthwestSteps(2),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASDb(bytearray(b"\xfd\xf2")),
                ASWalkSouthwestSteps(3),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASDb(bytearray(b"\xfd\xf2")),
                ASWalkSouthwestSteps(4),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASDb(bytearray(b"\xfd\xf2")),
                ASWalkSouthwestSteps(5),
                ASVisibilityOff(),
            ],
        ),
        Return(identifier="EVENT_3343_ret_8"),
    ]
)
