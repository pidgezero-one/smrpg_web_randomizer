from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1395_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7053, 1, 'EVENT_1395_move_script_to_main_thread_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 2, 'EVENT_1395_move_script_to_main_thread_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_move_script_to_main_thread_3',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_set_bit_4',
        "command": 'set_bit',
        "args": [0x7049, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 15, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_face_north_3',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [35]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_5_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._005_BLOCK_SWITCH, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1395_tint_layers_6',
        "command": 'tint_layers',
        "args": [0x70, 0x68, 0x10, 0, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.MINUS_SUB]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_priority_set_7',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [], [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.MINUS_SUB]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_fade_out_music_to_volume_8',
        "command": 'fade_out_music_to_volume',
        "args": [4, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [120]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_10_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [32]
            },
        ]
    },
    {
        "identifier": 'EVENT_1395_summon_to_current_level_11',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_12',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_circle_mask_static_13',
        "command": 'circle_mask_static',
        "args": [AreaObjects.NPC_2, 0, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._054_GOODNIGHT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_restore_all_hp_15',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_restore_all_fp_16',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_17',
        "command": 'pause',
        "args": [110],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_tint_layers_18',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 0, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.MINUS_SUB]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_reset_priority_set_19',
        "command": 'reset_priority_set',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_apply_tile_mod_20',
        "command": 'apply_tile_mod',
        "args": [Rooms._189_MARIOS_PIPEHOUSE, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_play_sound_21',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_22',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_24',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1395_action_queue_async_25_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1395_circle_mask_static_26',
        "command": 'circle_mask_static',
        "args": [AreaObjects.NPC_2, 35, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_27',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_play_sound_28',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_29',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_31',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1395_action_queue_async_32_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 6]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_32_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_32_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_32_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1395_fade_out_music_to_volume_33',
        "command": 'fade_out_music_to_volume',
        "args": [6, 100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_set_7000_to_tapped_button_34',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_pause_35',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_mem_7000_and_const_36',
        "command": 'mem_7000_and_const',
        "args": [0x0080],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_jmp_if_var_equals_short_37',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_1395_apply_tile_mod_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_1395_set_7000_to_tapped_button_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_apply_tile_mod_39',
        "command": 'apply_tile_mod',
        "args": [Rooms._189_MARIOS_PIPEHOUSE, 32, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_circle_mask_static_40',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 153, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1395_action_queue_async_41_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_41_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_41_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [120]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_41_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1395_action_queue_async_41_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1395_pause_42',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_play_sound_43',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_clear_bit_44',
        "command": 'clear_bit',
        "args": [0x7049, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1395_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
