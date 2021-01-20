from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3210_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_disable_trigger_1',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_temp_action_script_sync_2',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 337],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_add_4',
        "command": 'add',
        "args": [0x7000, 65533],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_add_7',
        "command": 'add',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_mem_704x_at_7000_bit_set_8',
        "command": 'jmp_if_mem_704x_at_7000_bit_set',
        "args": ['EVENT_3210_resume_action_script_82'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_mem_704x_at_7000_bit_10',
        "command": 'set_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_7000_to_object_coord_11',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A9, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 20, 'EVENT_3210_set_short_mem_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 21, 'EVENT_3210_set_short_mem_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 22, 'EVENT_3210_set_short_mem_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3210_jmp_if_bit_clear_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3210_jmp_if_bit_clear_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3210_jmp_if_bit_clear_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3210_ret_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_bit_clear_22',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_3210_ret_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_3210_ret_72'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_async_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_24_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [0, 103, 10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [2, 121, 0, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_set_palette_row_3',
                "command": 'set_palette_row',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_floating_on_5',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_25_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x98]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_set_7000_to_object_coord_26',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_7, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_dec_short_mem_27',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_loaded_memory_is_below_0_28',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_3210_mem_compare_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_mem_7000_xor_const_29',
        "command": 'mem_7000_xor_const',
        "args": [0xffff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_add_30',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_mem_compare_31',
        "command": 'mem_compare',
        "args": [0x7000, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_comparison_result_is_greater_or_equal_32',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3210_action_queue_sync_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_33_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_33_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_33_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_34_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [240]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_set_vram_priority_9',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_35_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0xd6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_set_7000_to_object_coord_36',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_7, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_dec_short_mem_37',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_loaded_memory_is_below_0_38',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_3210_mem_compare_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_mem_7000_xor_const_39',
        "command": 'mem_7000_xor_const',
        "args": [0xffff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_add_40',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_mem_compare_41',
        "command": 'mem_compare',
        "args": [0x7000, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_comparison_result_is_greater_or_equal_42',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3210_action_queue_sync_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_43_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_43_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_44_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [192]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_set_vram_priority_9',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_45_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x14]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_set_7000_to_object_coord_46',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_7, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_dec_short_mem_47',
        "command": 'dec_short_mem',
        "args": [0x7000, 0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_loaded_memory_is_below_0_48',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_3210_mem_compare_51'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_mem_7000_xor_const_49',
        "command": 'mem_7000_xor_const',
        "args": [0xffff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_add_50',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_mem_compare_51',
        "command": 'mem_compare',
        "args": [0x7000, 192],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_comparison_result_is_greater_or_equal_52',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3210_action_queue_sync_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_53_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_53_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_53_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_54_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [144]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_set_vram_priority_9',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_55_SUBSCRIPT_db_11',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x07, 0x52]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_jmp_if_objects_less_than_xy_steps_apart_same_z_coord_56',
        "command": 'jmp_if_objects_less_than_xy_steps_apart_same_z_coord',
        "args": [AreaObjects.NPC_7, AreaObjects.NPC_6, 0x00, 0x01, 0x2863],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_3210_action_queue_sync_73'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_bit_58',
        "command": 'set_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_action_script_sync_59',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 316],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 316],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_action_script_sync_61',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 316],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_pause_62',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 338],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_if_bit_set_64',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 1, 'EVENT_3210_action_queue_async_71'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_65',
        "command": 'set_short',
        "args": [0x7010, 0x0006],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_66',
        "command": 'set_short',
        "args": [0x7012, 0x0078],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_set_short_67',
        "command": 'set_short',
        "args": [0x7014, 0x0010],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_db_68',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_pause_69',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_create_packet_event_at_coords_jmp_if_null_70',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._035_FLOWER_JUMPS, 0x0cd9, 'EVENT_3210_pause_69'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x80]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x7016, 0xfffc]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_mem_compare_2',
                "command": 'mem_compare',
                "args": [0x7022, 0]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_jmp_if_loaded_memory_is_below_0_3',
                "command": 'jmp_if_loaded_memory_is_below_0',
                "args": ['EVENT_3210_action_queue_async_71_SUBSCRIPT_add_short_5']
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_set_short_4',
                "command": 'set_short',
                "args": [0x7016, 0x0000]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_add_short_5',
                "command": 'add_short',
                "args": [0x7018, 0xfff0]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_3210_action_queue_async_71_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_ret_72',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3210_action_queue_sync_73_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3210_resume_action_script_74',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_resume_action_script_75',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_resume_action_script_76',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_clear_bit_78',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_play_sound_80',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_3210_action_queue_async_71'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_resume_action_script_82',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_clear_mem_704x_at_7000_bit_83',
        "command": 'clear_mem_704x_at_7000_bit',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3210_ret_84',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
