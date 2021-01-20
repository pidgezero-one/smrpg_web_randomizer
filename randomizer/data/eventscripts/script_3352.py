from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3352_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_2_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [5, 102]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_2_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_3_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [1, 75]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_run_dialog_4',
        "command": 'run_dialog',
        "args": [1840, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_dialog_option_b_5',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3352_set_bit_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_run_dialog_6',
        "command": 'run_dialog',
        "args": [1841, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_bit_7',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_fade_out_music_to_volume_8',
        "command": 'fade_out_music_to_volume',
        "args": [4, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_9',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_music_default_volume_10',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_11',
        "command": 'set_short',
        "args": [0x7038, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_12',
        "command": 'set_short',
        "args": [0x703a, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_13',
        "command": 'set_short',
        "args": [0x703c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_14',
        "command": 'set_short',
        "args": [0x7024, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3352_clear_bit_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_7000_to_object_coord_16',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_mem_compare_17',
        "command": 'mem_compare',
        "args": [0x7000, 1024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_loaded_memory_is_below_0_18',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_3352_clear_bit_111'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_dec_short_19',
        "command": 'dec_short',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_loaded_memory_is_not_0_20',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3352_jmp_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_music_default_volume_23',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_slow_down_music_24',
        "command": 'slow_down_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_run_dialog_25',
        "command": 'run_dialog',
        "args": [1887, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_bit_26',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_27_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_27_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_28_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_pause_29',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_fade_out_to_black_async_30',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_to_event_31',
        "command": 'jmp_to_event',
        "args": [3356],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_random_above_66_33',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_3352_set_short_43'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_34',
        "command": 'set_short',
        "args": [0x7034, 0x0732],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x7038, 0x7036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_36',
        "command": 'set_short',
        "args": [0x7032, 0x0010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_to_subroutine_37',
        "command": 'jmp_to_subroutine',
        "args": [0x4db5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_3352_clear_bit_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x7036, 0x7038],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_set_40',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3352_pause_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_dialog_option_b_or_c_41',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3352_pause_103', 'EVENT_3352_pause_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_3352_pause_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_43',
        "command": 'set_short',
        "args": [0x7034, 0x0742],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x703a, 0x7036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_45',
        "command": 'set_short',
        "args": [0x7032, 0x0010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_to_subroutine_46',
        "command": 'jmp_to_subroutine',
        "args": [0x4db5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_set_47',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_3352_clear_bit_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_48',
        "command": 'set_short_mem',
        "args": [0x7036, 0x703a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_set_49',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3352_pause_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_dialog_option_b_or_c_50',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3352_pause_99', 'EVENT_3352_pause_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_3352_pause_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_52',
        "command": 'set_short',
        "args": [0x7034, 0x0752],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x703c, 0x7036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_54',
        "command": 'set_short',
        "args": [0x7032, 0x0008],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_to_subroutine_55',
        "command": 'jmp_to_subroutine',
        "args": [0x4db5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_set_56',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_3352_clear_bit_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_57',
        "command": 'set_short_mem',
        "args": [0x7036, 0x703c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_set_58',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3352_pause_107'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_dialog_option_b_or_c_59',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3352_pause_103', 'EVENT_3352_pause_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_3352_pause_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_61',
        "command": 'set_short',
        "args": [0x7026, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_generate_random_num_from_range_var_62',
        "command": 'generate_random_num_from_range_var',
        "args": [0x7032],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x703e, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_var_equals_short_64',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3352_set_short_mem_68'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_object_memory_to_65',
        "command": 'set_object_memory_to',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_mem_7000_shift_left_66',
        "command": 'mem_7000_shift_left',
        "args": [0x7026, 255],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_end_loop_67',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_68',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_mem_7000_and_var_69',
        "command": 'mem_7000_and_var',
        "args": [0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_mem_compare_70',
        "command": 'mem_compare',
        "args": [0x7000, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_loaded_memory_is_not_0_71',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_3352_set_bit_97'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_72',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7036],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_mem_7000_or_var_73',
        "command": 'mem_7000_or_var',
        "args": [0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_74',
        "command": 'set_short_mem',
        "args": [0x7036, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_mem_75',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_add_short_mem_76',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7034],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_action_script_sync_78',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_run_dialog_79',
        "command": 'run_dialog',
        "args": [0x7000, AreaObjects.NPC_12, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_clear_bit_80',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_script_resume_on_next_dialog_page_a_81',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_bit_82',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_83',
        "command": 'set_short',
        "args": [0x7028, 0x001e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_start_loop_n_frames_84',
        "command": 'start_loop_n_frames',
        "args": [299],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_85',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_random_86',
        "command": 'set_random',
        "args": [0x7000, 256],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_add_short_87',
        "command": 'add_short',
        "args": [0x7028, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_var_not_equals_short_88',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 60, 'EVENT_3352_if_0210_bits_012_clear_do_not_jump_91'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_sound_89',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_short_90',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_if_0210_bits_012_clear_do_not_jump_91',
        "command": 'if_0210_bits_012_clear_do_not_jump',
        "args": ['EVENT_3352_end_loop_93'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_3352_close_dialog_95'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_end_loop_93',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_bit_94',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_close_dialog_95',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_ret_96',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_bit_97',
        "command": 'set_bit',
        "args": [0x7044, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_ret_98',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_99',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_sound_100',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_action_queue_async_101',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_async_101_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_jmp_102',
        "command": 'jmp',
        "args": ['EVENT_3352_set_7000_to_object_coord_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_103',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_sound_104',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_async_105_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [14]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_jmp_106',
        "command": 'jmp',
        "args": ['EVENT_3352_set_7000_to_object_coord_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_107',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_sound_108',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_action_queue_async_109',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_async_109_SUBSCRIPT_shift_z_down_pixels_0',
                "command": 'shift_z_down_pixels',
                "args": [7]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_jmp_110',
        "command": 'jmp',
        "args": ['EVENT_3352_set_7000_to_object_coord_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_clear_bit_111',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_113',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_music_default_volume_114',
        "command": 'play_music_default_volume',
        "args": [Music._09_VICTORY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_run_dialog_115',
        "command": 'run_dialog',
        "args": [1886, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_set_bit_116',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_117',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_119',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_add_z_coord_1_step_2',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_119_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_action_queue_sync_120',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [256]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3352_action_queue_sync_120_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_object_memory_modify_bits_6',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_set_bit_7',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_shift_northeast_steps_9',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3352_action_queue_sync_120_SUBSCRIPT_set_bit_10',
                "command": 'set_bit',
                "args": [0x7044, 5]
            },
        ]
    },
    {
        "identifier": 'EVENT_3352_pause_121',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_clear_122',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'EVENT_3352_pause_121'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_play_sound_123',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_apply_tile_mod_124',
        "command": 'apply_tile_mod',
        "args": [Rooms._464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_pause_125',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_jmp_if_bit_clear_126',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_3352_pause_125'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_enter_area_127',
        "command": 'enter_area',
        "args": [Rooms._463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING, RadialDirections.NORTHEAST, 2, 55, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3352_ret_128',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
