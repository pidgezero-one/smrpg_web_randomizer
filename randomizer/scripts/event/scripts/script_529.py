# pylint: disable=C0301

"""E0529_ROSE_TOWN_OCCUPIED_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xfdG")),
        CloseDialog(),
        FadeOutMusicToVolume(duration=1, volume=127),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=10, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASSetPriority(2),
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
            ]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetPriority(2),
                ASJmpIfBitSet(
                    UNKNOWN_ROSE_TOWN_7060_0,
                    ["EVENT_529_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_4"]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASJmp(["EVENT_529_action_queue_sync_5"]),
                ASTransferToXYZF(
                    x=12,
                    y=47,
                    z=2,
                    direction=EAST,
                    identifier="EVENT_529_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_4"),
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
                ASJmpIfBitClear(
                    FREEZE_ROSE_TOWN_NPC_1, ["EVENT_529_action_queue_sync_6"]
                ),
                ASSetPriority(2),
            ],
            identifier="EVENT_529_action_queue_sync_5"),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(index=10, is_sequence=True, looping=True),
                ASSetPriority(3),
            ],
            identifier="EVENT_529_action_queue_sync_6"),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetPriority(3),
            ]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetPriority(3),
            ]),
        JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_1, ["EVENT_529_jmp_if_bit_set_177"]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkNortheastSteps(2)]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferXYZFPixels(x=240, y=8, z=0, direction=EAST),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNortheast(),
                ASSetPriority(2),
            ]),
        SetSyncActionScript(NPC_7, A0637_ROSE_TOWN_INITIAL_ARROW),
        SetBit(FREEZE_ROSE_TOWN_NPC_1),
        JmpIfBitSet(
            FREEZE_ROSE_TOWN_NPC_2,
            ["EVENT_529_set_7000_to_70A0_short_mem_181"],
            identifier="EVENT_529_jmp_if_bit_set_177"),
        ActionQueueSync(
            target=NPC_2, subscript=[ASSetSolidityBits(cant_pass_walls=True)]
        ),
        SetSyncActionScript(NPC_2, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
        Jmp(["EVENT_529_fade_in_from_black_async_197"]),
        CopyVarToVar(
            from_var=TEMP_70B8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_529_set_7000_to_70A0_short_mem_181"),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_529_set_7000_to_70A0_short_mem_190"]
        ),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=X_COORD_2,
            identifier="EVENT_529_set_7000_short_mem_to_7000_183"),
        CopyVarToVar(from_var=ROSE_TOWN_ARROW_POSITION, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_2),
        SetVarToConst(Z_COORD_2, 2),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
                ASDb(bytearray(b"\x9a")),
                ASJmpIfBitSet(
                    TEMP_7043_2,
                    [
                        "EVENT_529_action_queue_async_187_SUBSCRIPT_set_sprite_sequence_6"
                    ]),
                ASFaceNorthwest(),
                ASTransferXYZFPixels(x=240, y=248, z=0, direction=EAST),
                ASJmp(
                    ["EVENT_529_action_queue_async_187_SUBSCRIPT_fixed_f_coord_on_8"]
                ),
                ASSetSpriteSequence(
                    index=10,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_529_action_queue_async_187_SUBSCRIPT_set_sprite_sequence_6"),
                ASTransferXYZFPixels(x=16, y=8, z=0, direction=EAST),
                ASFixedFCoordOn(
                    identifier="EVENT_529_action_queue_async_187_SUBSCRIPT_fixed_f_coord_on_8"
                ),
            ]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_529_run_background_event_207"]),
        Jmp(["EVENT_529_fade_in_from_black_async_197"]),
        CopyVarToVar(
            from_var=TEMP_70B8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_529_set_7000_to_70A0_short_mem_190"),
        Mem7000AndConst(0x007F),
        SetBit(TEMP_7043_2),
        Jmp(["EVENT_529_set_7000_short_mem_to_7000_183"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_529_fade_in_from_black_async_197"
        ),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_529_run_background_event_207"]
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_529_run_background_event_207"]),
        RunEventAsSubroutine(E3895_ROSE_TOWN_STAR_PIECE_SIGNAL),
        RunBackgroundEvent(
            event_id=E0530_ROSE_TOWN_OCCUPIED_BACKGROUND_1,
            return_on_level_exit=True,
            identifier="EVENT_529_run_background_event_207"),
        RunBackgroundEvent(
            event_id=E0551_ROSE_TOWN_OCCUPIED_MODS,
            return_on_level_exit=True,
            bit_6=True),
        JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_1, ["EVENT_256_ret_0"]),
        Pause(10),
        Return(),
    ]
)
