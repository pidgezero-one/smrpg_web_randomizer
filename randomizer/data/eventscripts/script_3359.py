from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3359_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_0_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_0_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [23, 81]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_0_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_1_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_1_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_1_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_1_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [24, 79]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_2_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3359_run_dialog_5',
        "command": 'run_dialog',
        "args": [1904, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3359_jmp_if_dialog_option_b_6',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3359_set_bit_8']
    },
    {
        "identifier": 'EVENT_3359_run_dialog_7',
        "command": 'run_dialog',
        "args": [1905, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3359_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_set_short_9',
        "command": 'set_short',
        "args": [0x703c, 0x0015]
    },
    {
        "identifier": 'EVENT_3359_play_music_default_volume_10',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION]
    },
    {
        "identifier": 'EVENT_3359_freeze_camera_11',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3359_move_script_to_background_thread_2_12',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_3359_set_short_13',
        "command": 'set_short',
        "args": [0x703a, 0x0004]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_14_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3359_set_7000_to_tapped_button_16',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_3359_dec_short_21']
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703a, 4, 'EVENT_3359_pause_15']
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 32, 'EVENT_3359_action_queue_async_26']
    },
    {
        "identifier": 'EVENT_3359_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3359_pause_15']
    },
    {
        "identifier": 'EVENT_3359_dec_short_21',
        "command": 'dec_short',
        "args": [0x703a]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_22_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_22_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_22_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3359_action_queue_async_22_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_22_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703c, 0, 'EVENT_3359_resume_action_script_61']
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703a, 0, 'EVENT_3359_action_queue_async_26']
    },
    {
        "identifier": 'EVENT_3359_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3359_pause_15']
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_26_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_29_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_29_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_29_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_29_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_29_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_29_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_set_bit_30',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_set_random_31',
        "command": 'set_random',
        "args": [0x703a, 4]
    },
    {
        "identifier": 'EVENT_3359_add_short_32',
        "command": 'add_short',
        "args": [0x703a, 0x01]
    },
    {
        "identifier": 'EVENT_3359_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_33_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_pause_34',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3359_run_background_event_35',
        "command": 'run_background_event',
        "args": [3360, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3359_pause_36',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_equals_short_37',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703c, 0, 'EVENT_3359_resume_action_script_42']
    },
    {
        "identifier": 'EVENT_3359_dec_short_38',
        "command": 'dec_short',
        "args": [0x703a]
    },
    {
        "identifier": 'EVENT_3359_jmp_if_var_not_equals_short_39',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x703a, 0, 'EVENT_3359_action_queue_sync_33']
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_40_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_40_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_40_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_40_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_40_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_3359_set_short_13']
    },
    {
        "identifier": 'EVENT_3359_resume_action_script_42',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3359_pause_43',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3359_clear_bit_44',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3359_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 4]
    },
    {
        "identifier": 'EVENT_3359_pause_47',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3359_play_music_default_volume_48',
        "command": 'play_music_default_volume',
        "args": [Music._09_VICTORY]
    },
    {
        "identifier": 'EVENT_3359_run_dialog_49',
        "command": 'run_dialog',
        "args": [1908, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3359_set_bit_50',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_pause_51',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_3359_unfreeze_camera_52',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3359_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3359_action_queue_sync_53_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_54',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_54_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_54_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_54_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [29, 70]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_54_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_54_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_play_sound_55',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 4]
    },
    {
        "identifier": 'EVENT_3359_apply_tile_mod_56',
        "command": 'apply_tile_mod',
        "args": [Rooms._467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_57_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_57_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_set_short_58',
        "command": 'set_short',
        "args": [0x703e, 0x0000]
    },
    {
        "identifier": 'EVENT_3359_enter_area_59',
        "command": 'enter_area',
        "args": [Rooms._465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES, RadialDirections.NORTHEAST, 22, 33, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3359_ret_60',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3359_resume_action_script_61',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_3359_pause_62',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3359_play_sound_63',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 4]
    },
    {
        "identifier": 'EVENT_3359_pause_64',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3359_play_music_default_volume_65',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME]
    },
    {
        "identifier": 'EVENT_3359_slow_down_music_66',
        "command": 'slow_down_music'
    },
    {
        "identifier": 'EVENT_3359_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3359_action_queue_async_67_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3359_action_queue_async_67_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3359_clear_bit_68',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_set_action_script_sync_69',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3359_run_dialog_70',
        "command": 'run_dialog',
        "args": [1907, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3359_set_bit_71',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3359_pause_72',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'EVENT_3359_fade_out_to_black_async_73',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3359_jmp_to_event_74',
        "command": 'jmp_to_event',
        "args": [3356]
    }
]
