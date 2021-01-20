from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2100_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_2100_run_dialog_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2100_run_dialog_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_run_dialog_2',
        "command": 'run_dialog',
        "args": [2575, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_open_shop_3',
        "command": 'open_shop',
        "args": [Shops._18_NIMBUS_LAND_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_run_dialog_6',
        "command": 'run_dialog',
        "args": [2576, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2100_run_dialog_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_store_coin_amount_7000_8',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_mem_compare_9',
        "command": 'mem_compare',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_jmp_if_comparison_result_is_greater_or_equal_10',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2100_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_run_dialog_11',
        "command": 'run_dialog',
        "args": [2578, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_set_13',
        "command": 'set',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_dec_coins_14',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_run_dialog_15',
        "command": 'run_dialog',
        "args": [2580, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_fade_out_music_to_volume_16',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_circle_mask_static_17',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 18, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_pause_18',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._054_GOODNIGHT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_pause_20',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2100_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2100_pause_22',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_circle_mask_static_23',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_pause_24',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2100_action_queue_sync_25_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [8, 56, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2100_action_queue_sync_25_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2100_action_queue_sync_25_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2100_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2100_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2100_action_queue_sync_26_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2100_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2100_action_queue_async_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2100_action_queue_async_27_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [4, 41, 0]
            },
        ]
    },
    {
        "identifier": 'EVENT_2100_pause_28',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_circle_mask_static_29',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 40, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_pause_30',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_fade_out_music_to_volume_31',
        "command": 'fade_out_music_to_volume',
        "args": [6, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_pause_32',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_set_7000_to_tapped_button_33',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_pause_34',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_mem_7000_and_const_35',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_jmp_if_var_equals_short_36',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_2100_circle_mask_static_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_2100_set_7000_to_tapped_button_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_circle_mask_static_38',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 255, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2100_action_queue_async_39_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2100_action_queue_async_39_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2100_action_queue_async_39_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [120]
            },
            {
                "identifier": 'EVENT_2100_action_queue_async_39_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_2100_action_queue_async_39_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_2100_run_dialog_40',
        "command": 'run_dialog',
        "args": [2581, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2100_action_queue_async_41_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_2100_pause_42',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_restore_all_hp_43',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_restore_all_fp_44',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_run_dialog_46',
        "command": 'run_dialog',
        "args": [2579, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_ret_47',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_run_dialog_48',
        "command": 'run_dialog',
        "args": [2577, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_open_shop_49',
        "command": 'open_shop',
        "args": [Shops._19_HINOPIOS_SHOP],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_fade_in_from_black_async_50',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2100_ret_51',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
