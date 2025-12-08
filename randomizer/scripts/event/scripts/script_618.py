# pylint: disable=C0301

"""E0618_MARIO_AS_BELLHOP_TRIES_TO_GO_UPSTAIRS_WITHOUT_GUEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7044_5),
        JmpIfBitClear(TEMP_704C_0, ["EVENT_256_ret_0"]),
        ActionQueueAsync(target=NPC_5, subscript=[ASFaceNortheast()]),
        SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouth()]),
        RunDialog(
            dialog_id=DI1010_PLAYER_ESCORTS_GUEST,
            above_object=NPC_5,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ActionQueueAsync(target=NPC_5, subscript=[ASFaceNorthwest()]),
        Return(),
    ]
)
