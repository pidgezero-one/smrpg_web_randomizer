from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3355_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_random_2',
        "command": 'set_random',
        "args": [0x7000, 256],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_3',
        "command": 'run_dialog',
        "args": [1888, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_random_4',
        "command": 'set_random',
        "args": [0x7000, 256],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_5',
        "command": 'run_dialog',
        "args": [1889, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_7',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_8',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_9',
        "command": 'set_short',
        "args": [0x7024, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_10',
        "command": 'set_short',
        "args": [0x7026, 0x0016],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_11',
        "command": 'set_short',
        "args": [0x7028, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_subroutine_12',
        "command": 'jmp_to_subroutine',
        "args": [0x5030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_13',
        "command": 'run_dialog',
        "args": [1890, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_14',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x32, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_15',
        "command": 'set',
        "args": [0x7000, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_subroutine_16',
        "command": 'jmp_to_subroutine',
        "args": [0x5043],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_17',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_subroutine_18',
        "command": 'jmp_to_subroutine',
        "args": [0x5070],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703e, 2, 'EVENT_3355_jmp_if_dialog_option_b_or_c_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703e, 3, 'EVENT_3355_jmp_if_dialog_option_b_or_c_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_dialog_option_b_or_c_22',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3355_play_sound_28', 'EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_23',
        "command": 'jmp',
        "args": ['EVENT_3355_pause_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_dialog_option_b_or_c_24',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3355_pause_38', 'EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_dialog_option_b_or_c_26',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3355_play_sound_28', 'EVENT_3355_pause_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_27',
        "command": 'jmp',
        "args": ['EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_sound_28',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_slow_down_music_29',
        "command": 'slow_down_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_30_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_33',
        "command": 'run_dialog',
        "args": [1887, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_34',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_35',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_fade_out_to_black_async_36',
        "command": 'fade_out_to_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_event_37',
        "command": 'jmp_to_event',
        "args": [3356],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_38',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_sound_39',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_42',
        "command": 'run_dialog',
        "args": [1895, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_43',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_44',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_floating_off_9',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_shift_z_up_steps_10',
                "command": 'shift_z_up_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_45_SUBSCRIPT_walk_to_xy_coords_11',
                "command": 'walk_to_xy_coords',
                "args": [11, 42]
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_async_46_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_46_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_46_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_46_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_transfer_to_xyzf_9',
                "command": 'transfer_to_xyzf',
                "args": [13, 39, 16, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_start_loop_n_times_11',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_visibility_on_12',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_end_loop_16',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_47_SUBSCRIPT_visibility_on_17',
                "command": 'visibility_on',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_async_48_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_48_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_48_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_48_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_48_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_48_SUBSCRIPT_shift_z_up_steps_5',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_pause_49',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_50',
        "command": 'set_short',
        "args": [0x7024, 0x002b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_51',
        "command": 'set_short',
        "args": [0x7026, 0x001a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_52',
        "command": 'set_short',
        "args": [0x7028, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_subroutine_53',
        "command": 'jmp_to_subroutine',
        "args": [0x5030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_54',
        "command": 'run_dialog',
        "args": [1896, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_55',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x32, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_56',
        "command": 'set',
        "args": [0x7000, 19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_subroutine_57',
        "command": 'jmp_to_subroutine',
        "args": [0x5043],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_58',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_to_subroutine_59',
        "command": 'jmp_to_subroutine',
        "args": [0x5070],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_bit_set_60',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_var_equals_short_61',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703e, 2, 'EVENT_3355_jmp_if_dialog_option_b_or_c_65'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_var_equals_short_62',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703e, 3, 'EVENT_3355_jmp_if_dialog_option_b_or_c_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_dialog_option_b_or_c_63',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3355_play_sound_28', 'EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_3355_pause_69'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_dialog_option_b_or_c_65',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3355_pause_69', 'EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_dialog_option_b_or_c_67',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3355_play_sound_28', 'EVENT_3355_pause_69'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_68',
        "command": 'jmp',
        "args": ['EVENT_3355_play_sound_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_69',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_sound_70',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_71',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_73',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_music_default_volume_74',
        "command": 'play_music_default_volume',
        "args": [Music._09_VICTORY],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_75',
        "command": 'run_dialog',
        "args": [1897, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_76',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_77_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_async_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_78_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_78_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_78_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_play_sound_79',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_apply_tile_mod_80',
        "command": 'apply_tile_mod',
        "args": [Rooms._463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_async_81_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_3355_action_queue_async_81_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_enter_area_82',
        "command": 'enter_area',
        "args": [Rooms._466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM, RadialDirections.NORTHEAST, 12, 97, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_ret_83',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_mem_84',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_mem_85',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_object_memory_to_86',
        "command": 'set_object_memory_to',
        "args": [0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_random_above_128_87',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_3355_end_loop_91'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_88',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 279],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_short_89',
        "command": 'add_short',
        "args": [0x7024, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_90',
        "command": 'add',
        "args": [0x70a9, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_end_loop_91',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_ret_92',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_music_default_volume_93',
        "command": 'play_music_default_volume',
        "args": [Music._36_EXPLANATION],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_action_queue_sync_94',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_sync_94_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_94_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_pause_95',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_object_memory_to_96',
        "command": 'set_object_memory_to',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_97',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_sound_98',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_clear_bit_99',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_100',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_101',
        "command": 'run_dialog',
        "args": [1891, AreaObjects.NPC_14, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_102',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_103',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_dec_104',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_end_loop_105',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_106',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_sound_107',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3355_action_queue_sync_108_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3355_action_queue_sync_108_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
        ]
    },
    {
        "identifier": 'EVENT_3355_play_music_default_volume_109',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_ret_110',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_clear_bit_111',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_113',
        "command": 'run_dialog',
        "args": [1892, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_script_resume_on_next_dialog_page_a_114',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_115',
        "command": 'set_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_mem_116',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_117',
        "command": 'set_short',
        "args": [0x703e, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_random_above_66_118',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_3355_add_short_121'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_short_119',
        "command": 'add_short',
        "args": [0x703e, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_dec_120',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_short_121',
        "command": 'add_short',
        "args": [0x703e, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_dec_122',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_short_123',
        "command": 'add_short',
        "args": [0x703e, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_124',
        "command": 'run_dialog',
        "args": [1893, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_125',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_126',
        "command": 'run_dialog',
        "args": [1893, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_127',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_128',
        "command": 'run_dialog',
        "args": [1893, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_run_dialog_129',
        "command": 'run_dialog',
        "args": [1894, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_clear_bit_130',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_131',
        "command": 'set_short',
        "args": [0x7028, 0x001e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_start_loop_n_frames_132',
        "command": 'start_loop_n_frames',
        "args": [299],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_pause_133',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_random_134',
        "command": 'set_random',
        "args": [0x7000, 256],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_add_short_135',
        "command": 'add_short',
        "args": [0x7028, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_if_var_not_equals_short_136',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 60, 'EVENT_3355_if_0210_bits_012_clear_do_not_jump_139'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_play_sound_137',
        "command": 'play_sound',
        "args": [Sounds._144_CLICK, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_short_138',
        "command": 'set_short',
        "args": [0x7028, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_if_0210_bits_012_clear_do_not_jump_139',
        "command": 'if_0210_bits_012_clear_do_not_jump',
        "args": ['EVENT_3355_end_loop_141'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_jmp_140',
        "command": 'jmp',
        "args": ['EVENT_3355_close_dialog_143'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_end_loop_141',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_set_bit_142',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_close_dialog_143',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_db_144',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x32, 0x02, 0x07],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3355_ret_145',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]