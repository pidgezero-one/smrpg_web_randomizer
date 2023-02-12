# E3778_BALL_SOLITAIRE_SET_PUZZLE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ROSE_WAY_703E, 16),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASShiftXYPixels(x=250, y=253),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASShiftNortheastSteps(9)]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetSpriteSequence(index=3, looping=False), ASPause(38)],
        ),
        RunEventAsSubroutine(E3884_BALL_SOLITAIRE_SET_PUZZLE_CONFIGURATION_VALUE),
        JmpIf7000AnyBitsSet(destinations=["EVENT_3778_jmp_if_7000_any_bits_set_14"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_16"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_14",
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_18"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_16",
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_20"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_18",
        ),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_22"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_20",
        ),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_24"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_22",
        ),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_26"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_24",
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_28"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_26",
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_30"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_28",
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_32"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_30",
        ),
        ActionQueueAsync(
            target=NPC_10,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_34"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_32",
        ),
        ActionQueueAsync(
            target=NPC_11,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_36"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_34",
        ),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_38"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_36",
        ),
        ActionQueueAsync(
            target=NPC_13,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_40"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_38",
        ),
        ActionQueueAsync(
            target=NPC_14,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_jmp_if_7000_any_bits_set_42"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_40",
        ),
        ActionQueueAsync(
            target=NPC_15,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3778_action_queue_async_44"],
            identifier="EVENT_3778_jmp_if_7000_any_bits_set_42",
        ),
        ActionQueueAsync(
            target=NPC_16,
            subscript=[
                ASDec(ROSE_WAY_703E),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASShiftSouthwestSteps(9)],
            identifier="EVENT_3778_action_queue_async_44",
        ),
        PlayMusicAtDefaultVolume(M36_EXPLANATION),
        Return(),
    ]
)
