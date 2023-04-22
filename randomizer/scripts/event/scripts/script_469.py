# pylint: disable=C0301

"""E0469_YOSTER_ISLE_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([LEFT, RIGHT, DOWN, UP]),
        ActionQueueAsync(target=MARIO, subscript=[ASSetWalkingSpeed(FAST)]),
        UnfreezeCamera(),
        ActionQueueAsync(
            target=NPC_9, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])]
        ),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP],
            identifier="EVENT_469_enable_controls_until_return_4",
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASTransferToObjectXY(MARIO)]),
        SetSyncActionScript(NPC_9, A0505_SLOW_SEQUENCE_LOOP),
        Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_7"),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_7000_to_pressed_button_83"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_7000_to_pressed_button_87"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_7000_to_pressed_button_91"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_7000_to_pressed_button_95"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_61"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_67"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_64"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_58"]
        ),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_469_action_queue_async_20"]),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_enable_controls_until_return_99"]
        ),
        Pause(1),
        Jmp(["EVENT_469_enable_controls_until_return_4"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_703E),
            ],
            identifier="EVENT_469_action_queue_async_20",
        ),
        Db(bytearray(b"\xc7\x80")),
        CopyVarToVar(from_var=Z_COORD_2, to_var=PRIMARY_TEMP_7000),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_469_enable_controls_until_return_4"]
        ),
        Db(bytearray(b"\xfd\xca")),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_469_action_queue_async_30"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 512, ["EVENT_469_action_queue_async_30"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 531, ["EVENT_469_action_queue_async_30"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 256, ["EVENT_469_action_queue_async_30"]
        ),
        Jmp(["EVENT_469_enable_controls_until_return_4"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASRunAwayShift()],
            identifier="EVENT_469_action_queue_async_30",
        ),
        CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 4),
        Mem7000AndConst(0x0007),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        EnableControlsUntilReturn([]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_469_set_action_script_sync_48"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 4, ["EVENT_469_set_action_script_sync_48"]
        ),
        SetSyncActionScript(NPC_9, A0289_MARIO_DISMOUNT_YOSHI),
        SetSyncActionScript(MARIO, A0288_MARIO_DISMOUNT_YOSHI),
        UnsyncActionScript(MARIO),
        Pause(1, identifier="EVENT_469_pause_41"),
        JmpIfMarioInAir(["EVENT_469_pause_41"]),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=2),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=4),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=6),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
        SetSyncActionScript(
            NPC_9,
            A0498_MUSHROOM_DERBY_UNKNOWN,
            identifier="EVENT_469_set_action_script_sync_48",
        ),
        SetSyncActionScript(MARIO, A0497_MUSHROOM_DERBY_UNKNOWN),
        UnsyncActionScript(MARIO),
        Pause(1, identifier="EVENT_469_pause_51"),
        JmpIfMarioInAir(["EVENT_469_pause_51"]),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=2),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=4),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=6),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
        SetSyncActionScript(
            NPC_9, A0211_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_58"
        ),
        SetAsyncActionScript(MARIO, A0230_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetSyncActionScript(
            NPC_9, A0212_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_61"
        ),
        SetAsyncActionScript(MARIO, A0231_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetSyncActionScript(
            NPC_9, A0213_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_64"
        ),
        SetAsyncActionScript(MARIO, A0232_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetSyncActionScript(
            NPC_9, A0217_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_67"
        ),
        SetAsyncActionScript(MARIO, A0233_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetSyncActionScript(
            NPC_9, A0218_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_70"
        ),
        SetAsyncActionScript(MARIO, A0234_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetSyncActionScript(
            NPC_9, A0219_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_73"
        ),
        SetAsyncActionScript(MARIO, A0235_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetBit(TEMP_7044_7, identifier="EVENT_469_set_bit_76"),
        SetSyncActionScript(NPC_9, A0220_GREEN_YOSHI),
        SetAsyncActionScript(MARIO, A0236_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        SetSyncActionScript(
            NPC_9, A0221_GREEN_YOSHI, identifier="EVENT_469_set_action_script_sync_80"
        ),
        SetAsyncActionScript(MARIO, A0237_RIDE_YOSHI),
        Jmp(["EVENT_469_set_7000_to_pressed_button_7"]),
        Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_83"),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_58"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_61"]
        ),
        Jmp(["EVENT_469_set_action_script_sync_70"]),
        Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_87"),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_64"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_67"]
        ),
        Jmp(["EVENT_469_set_action_script_sync_73"]),
        Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_91"),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_58"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_64"]
        ),
        Jmp(["EVENT_469_set_bit_76"]),
        Set7000ToPressedButton(identifier="EVENT_469_set_7000_to_pressed_button_95"),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_61"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_469_set_action_script_sync_67"]
        ),
        Jmp(["EVENT_469_set_action_script_sync_80"]),
        EnableControlsUntilReturn(
            [], identifier="EVENT_469_enable_controls_until_return_99"
        ),
        ActionQueueSync(target=MARIO, subscript=[ASJumpToHeight(108)]),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
                ASSet700CToObjectCoord(target_npc=NPC_9, coord=COORD_F, pixel=True),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7032),
                ASJmpIf700CAnyBitsSet(
                    bits=[],
                    destinations=[
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_jmp_if_700C_equals_short_5"
                    ],
                ),
                ASJmp(["EVENT_469_pause_102"]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    3,
                    [
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_set_animation_speed_11"
                    ],
                    identifier="EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_jmp_if_700C_equals_short_5",
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_set_animation_speed_14"
                    ],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    7,
                    [
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_set_animation_speed_17"
                    ],
                ),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                ),
                ASJmp(
                    [
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_pause_19"
                    ]
                ),
                ASSetSequenceSpeed(
                    FAST,
                    identifier="EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_set_animation_speed_11",
                ),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=False
                ),
                ASJmp(
                    [
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_pause_19"
                    ]
                ),
                ASSetSequenceSpeed(
                    FAST,
                    identifier="EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_set_animation_speed_14",
                ),
                ASSetSpriteSequence(
                    index=13, sprite_offset=1, is_sequence=True, looping=False
                ),
                ASJmp(
                    [
                        "EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_pause_19"
                    ]
                ),
                ASSetSequenceSpeed(
                    FAST,
                    identifier="EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_set_animation_speed_17",
                ),
                ASSetSpriteSequence(
                    index=13,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                ),
                ASPause(
                    34,
                    identifier="EVENT_469_start_embedded_action_script_async_F1_101_SUBSCRIPT_pause_19",
                ),
                ASResetProperties(),
            ],
        ),
        Pause(1, identifier="EVENT_469_pause_102"),
        JmpIfMarioInAir(["EVENT_469_pause_102"]),
        RememberLastObject(),
        Jmp(["EVENT_469_enable_controls_until_return_4"]),
    ]
)
