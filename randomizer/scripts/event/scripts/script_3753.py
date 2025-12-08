# pylint: disable=C0301

"""E3753_HOT_SPRINGS_LOBBY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(HOT_SPRING_GUARD_POSITION, ["EVENT_3753_jmp_if_bit_set_7"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=19, y=56, z=0, direction=EAST),
                ASFaceNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=20, y=53, z=0, direction=EAST),
                ASFaceSouthwest(),
            ]),
        RememberLastObject(),
        JmpIfBitSet(
            DIRECTIONAL_7049_0,
            ["EVENT_3584_ret_0"],
            identifier="EVENT_3753_jmp_if_bit_set_7"),
        JmpIfBitSet(TEMP_704A_2, ["EVENT_3753_clear_bit_11"]),
        FadeInFromBlack(sync=False),
        Return(),
        ClearBit(TEMP_704A_2, identifier="EVENT_3753_clear_bit_11"),
        Return(),
    ]
)
