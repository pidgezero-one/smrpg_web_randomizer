from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1556_set_short_0',
        "command": 'set_short',
        "args": [0x700e, 0x0018]
    },
    {
        "identifier": 'EVENT_1556_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_1556_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_1556_set_short_2',
        "command": 'set_short',
        "args": [0x700e, 0x0019]
    },
    {
        "identifier": 'EVENT_1556_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1556_ret_80']
    },
    {
        "identifier": 'EVENT_1556_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_1556_ret_80']
    },
    {
        "identifier": 'EVENT_1556_enable_controls_until_return_5',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1556_set_short_6',
        "command": 'set_short',
        "args": [0x7024, 0x0014]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1556_dec_short_mem_8',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1556_jmp_if_7000_any_bits_set_9',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_1556_set_bit_13']
    },
    {
        "identifier": 'EVENT_1556_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1556_clear_bit_11',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1556_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_1556_mem_7000_and_const_15']
    },
    {
        "identifier": 'EVENT_1556_set_bit_13',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1556_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1556_mem_7000_and_const_15',
        "command": 'mem_7000_and_const',
        "args": [0x0004]
    },
    {
        "identifier": 'EVENT_1556_add_short_mem_16',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_set_7000_to_object_coord_19',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70AA, Coords.F, []]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1556_pause_action_script_22',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1556_inc_23',
        "command": 'inc',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_1556_end_loop_24',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1556_jmp_fork_mario_on_object_25',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1556_set_short_mem_45', 'EVENT_1556_start_battle_700E_26']
    },
    {
        "identifier": 'EVENT_1556_start_battle_700E_26',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_1556_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1556_reset_and_choose_game_43']
    },
    {
        "identifier": 'EVENT_1556_set_28',
        "command": 'set',
        "args": [0x70af, 0]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_30',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_start_loop_n_times_31',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1556_reset_coords_32',
        "command": 'reset_coords',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1556_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 652]
    },
    {
        "identifier": 'EVENT_1556_inc_34',
        "command": 'inc',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_1556_end_loop_35',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1556_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1556_action_queue_sync_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_36_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1556_fade_in_from_black_async_37',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1556_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1556_clear_bit_41']
    },
    {
        "identifier": 'EVENT_1556_clear_bit_39',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1556_ret_40',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1556_clear_bit_41',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1556_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1556_reset_and_choose_game_43',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1556_ret_44',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_45',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_46',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1556_action_queue_sync_47_SUBSCRIPT_face_east_7C_0',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_47_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_47_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_47_SUBSCRIPT_walk_1_step_f_direction_3',
                "command": 'walk_1_step_f_direction'
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_47_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1556_inc_48',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_1556_jmp_if_var_not_equals_byte_49',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70af, 10, 'EVENT_1556_add_coins_57']
    },
    {
        "identifier": 'EVENT_1556_inc_50',
        "command": 'inc',
        "args": [0x70ab]
    },
    {
        "identifier": 'EVENT_1556_summon_to_current_level_at_marios_coords_51',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.MEM_70AB]
    },
    {
        "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._094_FROG_COIN, 4]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_set_700C_to_object_coord_5',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F, []]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_add_6',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_mem_700C_and_const_7',
                "command": 'mem_700C_and_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_mem_700C_xor_const_8',
                "command": 'mem_700C_xor_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_face_east_7C_9',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_floating_off_10',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_jump_to_height_11',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_shift_f_direction_steps_12',
                "command": 'shift_f_direction_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_52_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1556_dec_53',
        "command": 'dec',
        "args": [0x70ab]
    },
    {
        "identifier": 'EVENT_1556_run_dialog_54',
        "command": 'run_dialog',
        "args": [1049, AreaObjects.TOADSTOOL, [_0x60Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1556_add_frog_coins_55',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1556_jmp_56',
        "command": 'jmp',
        "args": ['EVENT_1556_pause_60']
    },
    {
        "identifier": 'EVENT_1556_add_coins_57',
        "command": 'add_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1556_summon_to_current_level_at_marios_coords_58',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.MEM_70AB]
    },
    {
        "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 4]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_set_700C_to_object_coord_5',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F, []]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_add_6',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_mem_700C_and_const_7',
                "command": 'mem_700C_and_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_mem_700C_xor_const_8',
                "command": 'mem_700C_xor_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_face_east_7C_9',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_floating_off_10',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0xb0, 0xff]
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_walk_1_step_f_direction_13',
                "command": 'walk_1_step_f_direction'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1556_start_embedded_action_script_sync_F1_59_SUBSCRIPT_bpl_26_27_28_15',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_1556_pause_60',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_61',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_62',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_start_loop_n_times_63',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1556_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_1556_action_queue_sync_64_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_64_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_1556_action_queue_sync_64_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_1556_inc_65',
        "command": 'inc',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_1556_pause_66',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1556_end_loop_67',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1556_dec_68',
        "command": 'dec',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_1556_stop_embedded_action_script_69',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_70',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1556_set_short_mem_71',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_1556_start_loop_n_times_72',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1556_resume_action_script_73',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1556_inc_74',
        "command": 'inc',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_1556_end_loop_75',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1556_jmp_if_bit_set_76',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1556_clear_bit_79']
    },
    {
        "identifier": 'EVENT_1556_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1556_ret_78',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1556_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1556_ret_80',
        "command": 'ret'
    }
]
