from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1745_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7010, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_set_700C_to_object_coord_6',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_mem_compare_7',
                "command": 'mem_compare',
                "args": [0x700c, 0x7010]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_jmp_if_comparison_result_is_lesser_8',
                "command": 'jmp_if_comparison_result_is_lesser',
                "args": ['EVENT_1745_action_queue_async_3_SUBSCRIPT_play_sound_10']
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_jump_to_height_11',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_3_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [32]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_set_short_4',
        "command": 'set_short',
        "args": [0x700e, 0x00ce],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_start_battle_700E_5',
        "command": 'start_battle_700E',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1745_action_queue_async_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_1745_reset_and_choose_game_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_remove_object_at_70A8_from_current_level_8',
        "command": 'remove_object_at_70A8_from_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_pause_9',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_disable_trigger_10',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_pause_12',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_13_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_13_SUBSCRIPT_shift_f_direction_pixels_2',
                "command": 'shift_f_direction_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_13_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_start_loop_n_times_18',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_sync_19_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_add_20',
        "command": 'add',
        "args": [0x70a8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_end_loop_21',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_pause_22',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_short_23',
        "command": 'set_short',
        "args": [0x701c, 0x005a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_run_background_event_with_pause_return_on_exit_24',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1789, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_bit_25',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_bit_26',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_unfreeze_all_npcs_27',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_reset_and_choose_game_29',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_ret_30',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xc8, 0x07]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_set_short_2',
                "command": 'set_short',
                "args": [0x701a, 0x0000]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_31_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_pause_action_script_32',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_reset_coords_33',
        "command": 'reset_coords',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_pause_34',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_7000_to_object_coord_35',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_set_700C_to_object_coord_2',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_mem_compare_3',
                "command": 'mem_compare',
                "args": [0x700c, 0x7012]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_jmp_if_comparison_result_is_greater_or_equal_4',
                "command": 'jmp_if_comparison_result_is_greater_or_equal',
                "args": ['EVENT_1745_action_queue_async_37_SUBSCRIPT_shift_south_pixels_7']
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_1745_action_queue_async_37_SUBSCRIPT_face_north_8']
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_shift_south_pixels_7',
                "command": 'shift_south_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_face_north_8',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_37_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_dec_38',
        "command": 'dec',
        "args": [0x70ae],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_temp_action_script_sync_39',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_fade_in_from_black_async_40',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_unfreeze_all_npcs_41',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_freeze_all_npcs_until_return_43',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_add_44',
        "command": 'add',
        "args": [0x70a8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_add_45',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_jmp_if_var_equals_byte_46',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 3, 'EVENT_1745_add_52'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_summon_to_current_level_at_marios_coords_47',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_set_700C_to_object_coord_5',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_add_6',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_mem_700C_and_const_7',
                "command": 'mem_700C_and_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_mem_700C_xor_const_8',
                "command": 'mem_700C_xor_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_face_east_9',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_floating_off_10',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x25, 0x00, 0x08, 0xb0, 0xff]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_walk_1_step_f_direction_13',
                "command": 'walk_1_step_f_direction',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_48_SUBSCRIPT_bpl_26_27_28_15',
                "command": 'bpl_26_27_28',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_sync_49_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_49_SUBSCRIPT_walk_1_step_f_direction_1',
                "command": 'walk_1_step_f_direction',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_add_coins_50',
        "command": 'add_coins',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_1745_unfreeze_all_npcs_58'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_add_52',
        "command": 'add',
        "args": [0x70a8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_summon_to_current_level_at_marios_coords_53',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._094_FROG_COIN, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_set_700C_to_object_coord_5',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_add_6',
                "command": 'add',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_mem_700C_and_const_7',
                "command": 'mem_700C_and_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_mem_700C_xor_const_8',
                "command": 'mem_700C_xor_const',
                "args": [0x0004]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_face_east_9',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_floating_off_10',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_jump_to_height_11',
                "command": 'jump_to_height',
                "args": [160]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_shift_f_direction_steps_12',
                "command": 'shift_f_direction_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_54_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_sync_55_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._094_FROG_COIN, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_55_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_55_SUBSCRIPT_walk_1_step_f_direction_2',
                "command": 'walk_1_step_f_direction',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_add_frog_coins_56',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_57',
        "command": 'set',
        "args": [0x70ae, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_unfreeze_all_npcs_58',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_ret_59',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_freeze_all_npcs_until_return_60',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_61',
        "command": 'set',
        "args": [0x70ae, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._093_JUMP_INTO_WATER, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._093_JUMP_INTO_WATER, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_jump_to_height_8',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._093_JUMP_INTO_WATER, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_shift_z_up_pixels_12',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_shift_z_down_pixels_13',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._093_JUMP_INTO_WATER, 4]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_visibility_off_16',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_db_17',
                "command": 'db',
                "args": [0xfd, 0xf2]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_clear_solidity_bits_18',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_sync_62_SUBSCRIPT_set_bit_19',
                "command": 'set_bit',
                "args": [0x7043, 4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_set_7000_to_object_coord_63',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_set_short_mem_64',
        "command": 'set_short_mem',
        "args": [0x7012, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_set_700C_to_object_coord_2',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_mem_compare_3',
                "command": 'mem_compare',
                "args": [0x700c, 0x7012]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_jmp_if_comparison_result_is_greater_or_equal_4',
                "command": 'jmp_if_comparison_result_is_greater_or_equal',
                "args": ['EVENT_1745_action_queue_async_65_SUBSCRIPT_shift_south_pixels_7']
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_1745_action_queue_async_65_SUBSCRIPT_face_north_8']
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_shift_south_pixels_7',
                "command": 'shift_south_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_face_north_8',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1745_action_queue_async_65_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1745_unfreeze_all_npcs_66',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1745_ret_67',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
