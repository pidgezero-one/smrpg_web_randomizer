from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3502_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3502_move_script_to_background_thread_2_1',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_3502_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3502_move_script_to_main_thread_32']
    },
    {
        "identifier": 'EVENT_3502_set_7000_to_pressed_button_4',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3502_jmp_if_7000_any_bits_set_5',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_3502_jmp_if_var_equals_short_24']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_7000_any_bits_set_6',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_3502_jmp_if_var_equals_short_24']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_7000_any_bits_set_7',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_3502_jmp_if_var_equals_short_28']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_3502_jmp_if_var_equals_short_28']
    },
    {
        "identifier": 'EVENT_3502_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_3502_move_script_to_main_thread_32']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_3502_pause_2']
    },
    {
        "identifier": 'EVENT_3502_mem_compare_12',
        "command": 'mem_compare',
        "args": [0x7024, 0]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_loaded_memory_is_0_13',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_3502_clear_bit_22']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_loaded_memory_is_above_or_equal_0_14',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['EVENT_3502_action_queue_async_20']
    },
    {
        "identifier": 'EVENT_3502_dec_short_15',
        "command": 'dec_short',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_var_not_equals_short_16',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 0, 'EVENT_3502_pause_2']
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_17_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_17_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_17_SUBSCRIPT_dec_short_3',
                "command": 'dec_short',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_17_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_set_short_18',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_3502_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_3502_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_20_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_20_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_20_SUBSCRIPT_add_short_3',
                "command": 'add_short',
                "args": [0x7024, 0x01]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_20_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_3502_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_3502_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3502_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_3502_pause_2']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7034, 40, 'EVENT_3502_pause_9']
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_25_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_add_short_26',
        "command": 'add_short',
        "args": [0x7034, 0x01]
    },
    {
        "identifier": 'EVENT_3502_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3502_jmp_if_bit_set_10']
    },
    {
        "identifier": 'EVENT_3502_jmp_if_var_equals_short_28',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7034, 0, 'EVENT_3502_pause_9']
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_29_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_dec_short_30',
        "command": 'dec_short',
        "args": [0x7034]
    },
    {
        "identifier": 'EVENT_3502_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_3502_jmp_if_bit_set_10']
    },
    {
        "identifier": 'EVENT_3502_move_script_to_main_thread_32',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_3502_freeze_all_npcs_until_return_33',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_3502_stop_all_background_events_34',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3502_db_35',
        "command": 'db',
        "args": [0xfd, 0x44]
    },
    {
        "identifier": 'EVENT_3502_stop_background_event_36',
        "command": 'stop_background_event',
        "args": [timer_memory=0x701c]
    },
    {
        "identifier": 'EVENT_3502_stop_background_event_37',
        "command": 'stop_background_event',
        "args": [timer_memory=0x701e]
    },
    {
        "identifier": 'EVENT_3502_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_1, 161]
    },
    {
        "identifier": 'EVENT_3502_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_2, 161]
    },
    {
        "identifier": 'EVENT_3502_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 161]
    },
    {
        "identifier": 'EVENT_3502_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 161]
    },
    {
        "identifier": 'EVENT_3502_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 161]
    },
    {
        "identifier": 'EVENT_3502_resume_action_script_43',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_3502_resume_action_script_44',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3502_resume_action_script_45',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_3502_start_embedded_action_script_async_46',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_3502_start_embedded_action_script_async_46_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_fade_out_music_to_volume_47',
        "command": 'fade_out_music_to_volume',
        "args": [5, 0]
    },
    {
        "identifier": 'EVENT_3502_db_48',
        "command": 'db',
        "args": [0xfd, 0x45]
    },
    {
        "identifier": 'EVENT_3502_enable_controls_until_return_49',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_bit_set_50',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 7, 'EVENT_3502_jmp_if_bit_set_78']
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_51',
        "command": 'apply_tile_mod',
        "args": [Rooms._054_BOOSTER_HILL_____DUMMY, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_52',
        "command": 'apply_tile_mod',
        "args": [Rooms._054_BOOSTER_HILL_____DUMMY, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_53',
        "command": 'apply_tile_mod',
        "args": [Rooms._054_BOOSTER_HILL_____DUMMY, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_stop_embedded_action_script_54',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.LAYER_1]
    },
    {
        "identifier": 'EVENT_3502_reset_coords_55',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3502_set_action_script_async_56',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_7, 160]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_57',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b1]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_var_equals_short_58',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3502_run_dialog_61']
    },
    {
        "identifier": 'EVENT_3502_run_dialog_59',
        "command": 'run_dialog',
        "args": [1189, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE]]
    },
    {
        "identifier": 'EVENT_3502_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_3502_action_queue_sync_62']
    },
    {
        "identifier": 'EVENT_3502_run_dialog_61',
        "command": 'run_dialog',
        "args": [1193, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE]]
    },
    {
        "identifier": 'EVENT_3502_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_sync_62_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_62_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_62_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_62_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_62_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_sync_63_SUBSCRIPT_shift_north_pixels_0',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_63_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_63_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_63_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3502_action_queue_sync_63_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_64_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_64_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_64_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_64_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_64_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_64_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 54, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_play_music_current_volume_65',
        "command": 'play_music_current_volume',
        "args": [Music._37_BOOSTER_HILL_START]
    },
    {
        "identifier": 'EVENT_3502_fade_out_music_to_volume_66',
        "command": 'fade_out_music_to_volume',
        "args": [3, 127]
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_fixed_f_coord_on_6',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_walk_1_step_southwest_7',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_fixed_f_coord_off_11',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_face_northwest_12',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_face_west_14',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_67_SUBSCRIPT_shift_southwest_steps_16',
                "command": 'shift_southwest_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_unfreeze_camera_68',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3502_unsync_dialog_69',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_3502_set_bit_70',
        "command": 'set_bit',
        "args": [0x704d, 7]
    },
    {
        "identifier": 'EVENT_3502_set_bit_71',
        "command": 'set_bit',
        "args": [0x7067, 0]
    },
    {
        "identifier": 'EVENT_3502_set_bit_72',
        "command": 'set_bit',
        "args": [0x706f, 0]
    },
    {
        "identifier": 'EVENT_3502_set_bit_73',
        "command": 'set_bit',
        "args": [0x7068, 4]
    },
    {
        "identifier": 'EVENT_3502_set_bit_74',
        "command": 'set_bit',
        "args": [0x7070, 4]
    },
    {
        "identifier": 'EVENT_3502_set_bit_75',
        "command": 'set_bit',
        "args": [0x7067, 1]
    },
    {
        "identifier": 'EVENT_3502_enter_area_76',
        "command": 'enter_area',
        "args": [Rooms._005_MARRYMORE_OUTSIDE_DURING_BOOSTER, RadialDirections.NORTHWEST, 8, 92, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3502_ret_77',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3502_jmp_if_bit_set_78',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 4, 'EVENT_3502_apply_tile_mod_121']
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_79',
        "command": 'apply_tile_mod',
        "args": [Rooms._014_BOOSTER_HILL, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_80',
        "command": 'apply_tile_mod',
        "args": [Rooms._014_BOOSTER_HILL, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_81',
        "command": 'apply_tile_mod',
        "args": [Rooms._014_BOOSTER_HILL, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_stop_embedded_action_script_82',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.LAYER_1]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_83',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_and_const_84',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_85',
        "command": 'set_short_mem',
        "args": [0x7032, 0x7000]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_86',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_shift_left_87',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_and_const_88',
        "command": 'mem_7000_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'EVENT_3502_add_short_mem_89',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7032]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_90',
        "command": 'set_short_mem',
        "args": [0x7032, 0x7000]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_91',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_shift_left_92',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 7]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_and_const_93',
        "command": 'mem_7000_and_const',
        "args": [0x0001]
    },
    {
        "identifier": 'EVENT_3502_add_short_mem_94',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7032]
    },
    {
        "identifier": 'EVENT_3502_jmp_if_var_equals_short_95',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3502_run_dialog_98']
    },
    {
        "identifier": 'EVENT_3502_run_dialog_96',
        "command": 'run_dialog',
        "args": [1190, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE]]
    },
    {
        "identifier": 'EVENT_3502_jmp_97',
        "command": 'jmp',
        "args": ['EVENT_3502_action_queue_async_99']
    },
    {
        "identifier": 'EVENT_3502_run_dialog_98',
        "command": 'run_dialog',
        "args": [1194, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE]]
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_99',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_99_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_99_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_99_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_99_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_99_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_99_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 54, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_play_music_current_volume_100',
        "command": 'play_music_current_volume',
        "args": [Music._37_BOOSTER_HILL_START]
    },
    {
        "identifier": 'EVENT_3502_fade_out_music_to_volume_101',
        "command": 'fade_out_music_to_volume',
        "args": [3, 127]
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_102_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_102_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_102_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_102_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_102_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_102_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_unfreeze_camera_103',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3502_unsync_dialog_104',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_3502_jmp_if_var_equals_byte_105',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b2, 0, 'EVENT_3502_set_bit_117']
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_106',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_and_const_107',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3502_run_dialog_108',
        "command": 'run_dialog',
        "args": [1195, AreaObjects.TOADSTOOL, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_109',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_shift_left_110',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_and_const_111',
        "command": 'mem_7000_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'EVENT_3502_run_dialog_duration_112',
        "command": 'run_dialog_duration',
        "args": [1196, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3502_set_short_mem_113',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b2]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_shift_left_114',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 7]
    },
    {
        "identifier": 'EVENT_3502_mem_7000_and_const_115',
        "command": 'mem_7000_and_const',
        "args": [0x0001]
    },
    {
        "identifier": 'EVENT_3502_run_dialog_duration_116',
        "command": 'run_dialog_duration',
        "args": [1197, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3502_set_bit_117',
        "command": 'set_bit',
        "args": [0x7068, 4]
    },
    {
        "identifier": 'EVENT_3502_set_bit_118',
        "command": 'set_bit',
        "args": [0x704e, 1]
    },
    {
        "identifier": 'EVENT_3502_open_location_119',
        "command": 'open_location',
        "args": [Locations._027_BOOSTER_HILL, [6, 7]]
    },
    {
        "identifier": 'EVENT_3502_ret_120',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_121',
        "command": 'apply_tile_mod',
        "args": [Rooms._014_BOOSTER_HILL, 34, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_122',
        "command": 'apply_tile_mod',
        "args": [Rooms._014_BOOSTER_HILL, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_apply_tile_mod_123',
        "command": 'apply_tile_mod',
        "args": [Rooms._014_BOOSTER_HILL, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3502_stop_embedded_action_script_124',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.LAYER_1]
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_125',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_125_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_125_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_125_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_125_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_125_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_125_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [5, 54, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3502_action_queue_async_126_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_126_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_126_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_126_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_126_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3502_action_queue_async_126_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3502_unfreeze_camera_127',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3502_set_bit_128',
        "command": 'set_bit',
        "args": [0x7068, 4]
    },
    {
        "identifier": 'EVENT_3502_run_dialog_129',
        "command": 'run_dialog',
        "args": [1198, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3502_open_location_130',
        "command": 'open_location',
        "args": [Locations._027_BOOSTER_HILL, [6, 7]]
    },
    {
        "identifier": 'EVENT_3502_ret_131',
        "command": 'ret'
    }
]
