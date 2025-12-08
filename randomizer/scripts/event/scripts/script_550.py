# pylint: disable=C0301

"""E0550_ROSE_TOWN_OCCUPIED_ARROW_CONTROL_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_ROSE_TOWN_7060_0, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7044_3, ["EVENT_256_ret_0"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        CompareVarToConst(TEMP_7026, 3),
        JmpIfComparisonResultIsLesser(["EVENT_550_set_bit_8"]),
        CompareVarToConst(TEMP_7026, 6),
        JmpIfComparisonResultIsLesser(["EVENT_256_ret_0"]),
        SetBit(UNKNOWN_ROSE_TOWN_7060_0, identifier="EVENT_550_set_bit_8"),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(30),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalkNorthwestSteps(2),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASSetSolidityBits(cant_walk_through=True),
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
            ]),
        SetSyncActionScript(NPC_7, A0638_ROSE_TOWN_ARROW),
        Return(),
    ]
)
