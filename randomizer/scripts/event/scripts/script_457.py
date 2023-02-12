# E0457_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
            identifier="EVENT_457_action_queue_sync_0",
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSequenceLoopingOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSequenceLoopingOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSequenceLoopingOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        RememberLastObject(),
        Return(),
    ]
)
