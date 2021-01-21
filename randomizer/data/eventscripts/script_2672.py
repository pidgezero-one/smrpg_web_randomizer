from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2672_set_2']
    },
    {
        "identifier": 'EVENT_2672_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xc8, 0x94]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_add_short_1',
                "command": 'add_short',
                "args": [0x7018, 0x0002]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2672_action_queue_async_1_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_face_north_6',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_1_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_set_2',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_2672_resume_action_script_3',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_4_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [244, 1, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_5_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [12, 1, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_remember_last_object_6',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 0, 'EVENT_2672_run_dialog_27']
    },
    {
        "identifier": 'EVENT_2672_set_bit_8',
        "command": 'set_bit',
        "args": [0x705f, 0]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_9',
        "command": 'run_dialog',
        "args": [2544, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_play_music_default_volume_10',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_11',
        "command": 'run_dialog',
        "args": [2545, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_face_east_2',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_shift_northwest_pixels_9',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_face_north_10',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_12_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_pause_13',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_14',
        "command": 'run_dialog',
        "args": [2546, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_remember_last_object_15',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_2672_jmp_if_dialog_option_b_16',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2672_pause_22']
    },
    {
        "identifier": 'EVENT_2672_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2672_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2672_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_20',
        "command": 'run_dialog',
        "args": [2548, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_2672_set_action_script_sync_35']
    },
    {
        "identifier": 'EVENT_2672_pause_22',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2672_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_2672_pause_24',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_25',
        "command": 'run_dialog',
        "args": [2549, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_run_dialog_27',
        "command": 'run_dialog',
        "args": [2547, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_dialog_option_b_28',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2672_pause_30']
    },
    {
        "identifier": 'EVENT_2672_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_2672_pause_17']
    },
    {
        "identifier": 'EVENT_2672_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2672_set_action_script_async_31',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_2672_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_33',
        "command": 'run_dialog',
        "args": [2553, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 893]
    },
    {
        "identifier": 'EVENT_2672_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_36_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_36_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70c9]
    },
    {
        "identifier": 'EVENT_2672_set_short_mem_38',
        "command": 'set_short_mem',
        "args": [0x702c, 0x7000]
    },
    {
        "identifier": 'EVENT_2672_mem_compare_39',
        "command": 'mem_compare',
        "args": [0x702c, 10]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_greater_or_equal_40',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2672_set_random_54']
    },
    {
        "identifier": 'EVENT_2672_mem_compare_41',
        "command": 'mem_compare',
        "args": [0x702c, 5]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_greater_or_equal_42',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2672_set_random_48']
    },
    {
        "identifier": 'EVENT_2672_set_random_43',
        "command": 'set_random',
        "args": [0x702a, 5]
    },
    {
        "identifier": 'EVENT_2672_mem_compare_44',
        "command": 'mem_compare',
        "args": [0x702a, 1]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_lesser_45',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2672_set_random_43']
    },
    {
        "identifier": 'EVENT_2672_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_load_mem_1',
                "command": 'load_mem',
                "args": [0x702a]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_jmp_if_random_above_128_7',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_13']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_bit_10',
                "command": 'set_bit',
                "args": [0x7044, 5]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_clear_bit_11',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_jmp_12',
                "command": 'jmp',
                "args": ['EVENT_2672_jmp_47']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_set_bit_17',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_46_SUBSCRIPT_clear_bit_18',
                "command": 'clear_bit',
                "args": [0x7044, 5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_2672_action_queue_async_59']
    },
    {
        "identifier": 'EVENT_2672_set_random_48',
        "command": 'set_random',
        "args": [0x702a, 7]
    },
    {
        "identifier": 'EVENT_2672_mem_compare_49',
        "command": 'mem_compare',
        "args": [0x702a, 1]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_lesser_50',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2672_set_random_48']
    },
    {
        "identifier": 'EVENT_2672_set_bit_51',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_2672_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_load_mem_1',
                "command": 'load_mem',
                "args": [0x702a]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_jmp_if_random_above_128_7',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_13']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_bit_10',
                "command": 'set_bit',
                "args": [0x7044, 5]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_clear_bit_11',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_jmp_12',
                "command": 'jmp',
                "args": ['EVENT_2672_jmp_53']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_set_bit_17',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_52_SUBSCRIPT_clear_bit_18',
                "command": 'clear_bit',
                "args": [0x7044, 5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_2672_action_queue_async_59']
    },
    {
        "identifier": 'EVENT_2672_set_random_54',
        "command": 'set_random',
        "args": [0x702a, 7]
    },
    {
        "identifier": 'EVENT_2672_mem_compare_55',
        "command": 'mem_compare',
        "args": [0x702a, 1]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_lesser_56',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2672_set_random_54']
    },
    {
        "identifier": 'EVENT_2672_set_bit_57',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_2672_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_load_mem_1',
                "command": 'load_mem',
                "args": [0x702a]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_end_loop_18',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_jmp_if_random_above_128_19',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_27']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_bit_24',
                "command": 'set_bit',
                "args": [0x7044, 5]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_clear_bit_25',
                "command": 'clear_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_jmp_26',
                "command": 'jmp',
                "args": ['EVENT_2672_action_queue_async_59']
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_33',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_34',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_35',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_36',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_37',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_38',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_39',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_pause_40',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_set_bit_41',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_2672_action_queue_async_58_SUBSCRIPT_clear_bit_42',
                "command": 'clear_bit',
                "args": [0x7044, 5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_async_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 893]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_61',
        "command": 'run_dialog',
        "args": [2550, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_disable_trigger_62',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_63_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_64_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_set_bit_65',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2672_remember_last_object_66',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_2672_ret_67',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2672_play_sound_68',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_2672_set_short_mem_69',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70c9]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_var_equals_short_70',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2672_clear_bit_134']
    },
    {
        "identifier": 'EVENT_2672_run_dialog_71',
        "command": 'run_dialog',
        "args": [2551, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_add_72',
        "command": 'add',
        "args": [0x70c9, 0x01]
    },
    {
        "identifier": 'EVENT_2672_set_short_mem_73',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70c9]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 255, 'EVENT_2672_set_132']
    },
    {
        "identifier": 'EVENT_2672_clear_bit_75',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2672_jmp_77',
        "command": 'jmp',
        "args": ['EVENT_2672_set_random_93']
    },
    {
        "identifier": 'EVENT_2672_play_sound_78',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_79',
        "command": 'run_dialog',
        "args": [2552, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_set_short_mem_80',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70c9]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_var_equals_short_81',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2672_clear_bit_84']
    },
    {
        "identifier": 'EVENT_2672_dec_82',
        "command": 'dec',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_2672_set_short_mem_83',
        "command": 'set_short_mem',
        "args": [0x70c9, 0x7000]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_84',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2672_pause_script_resume_on_next_dialog_page_a_85',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_86',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_2672_set_action_script_sync_89']
    },
    {
        "identifier": 'EVENT_2672_set_action_script_sync_87',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 894]
    },
    {
        "identifier": 'EVENT_2672_jmp_88',
        "command": 'jmp',
        "args": ['EVENT_2672_unsync_dialog_90']
    },
    {
        "identifier": 'EVENT_2672_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 895]
    },
    {
        "identifier": 'EVENT_2672_unsync_dialog_90',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2672_set_action_script_sync_91',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 892]
    },
    {
        "identifier": 'EVENT_2672_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_set_random_93',
        "command": 'set_random',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_2672_mem_compare_94',
        "command": 'mem_compare',
        "args": [0x7000, 3]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_comparison_result_is_lesser_95',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_2672_jmp_if_bit_set_124']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_96',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_2672_set_100']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_97',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_2672_set_102']
    },
    {
        "identifier": 'EVENT_2672_set_98',
        "command": 'set',
        "args": [0x70a7, 155]
    },
    {
        "identifier": 'EVENT_2672_jmp_99',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_104']
    },
    {
        "identifier": 'EVENT_2672_set_100',
        "command": 'set',
        "args": [0x70a7, 156]
    },
    {
        "identifier": 'EVENT_2672_jmp_101',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_104']
    },
    {
        "identifier": 'EVENT_2672_set_102',
        "command": 'set',
        "args": [0x70a7, 157]
    },
    {
        "identifier": 'EVENT_2672_jmp_103',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_104']
    },
    {
        "identifier": 'EVENT_2672_play_sound_104',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_105',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_106',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_2672_put_inventory_110']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_107',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_2672_put_inventory_112']
    },
    {
        "identifier": 'EVENT_2672_put_inventory_108',
        "command": 'put_inventory',
        "args": [items.WiltShroom]
    },
    {
        "identifier": 'EVENT_2672_jmp_109',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_put_inventory_110',
        "command": 'put_inventory',
        "args": [items.RottenMush]
    },
    {
        "identifier": 'EVENT_2672_jmp_111',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_put_inventory_112',
        "command": 'put_inventory',
        "args": [items.MoldyMush]
    },
    {
        "identifier": 'EVENT_2672_jmp_113',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_play_sound_114',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_115',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_116',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_2672_put_inventory_120']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_117',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_2672_put_inventory_122']
    },
    {
        "identifier": 'EVENT_2672_put_inventory_118',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_2672_jmp_119',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_put_inventory_120',
        "command": 'put_inventory',
        "args": [items.MidMushroom]
    },
    {
        "identifier": 'EVENT_2672_jmp_121',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_put_inventory_122',
        "command": 'put_inventory',
        "args": [items.MaxMushroom]
    },
    {
        "identifier": 'EVENT_2672_jmp_123',
        "command": 'jmp',
        "args": ['EVENT_2672_clear_bit_144']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_124',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_2672_set_128']
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_125',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_2672_set_130']
    },
    {
        "identifier": 'EVENT_2672_set_126',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_2672_jmp_127',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_114']
    },
    {
        "identifier": 'EVENT_2672_set_128',
        "command": 'set',
        "args": [0x70a7, 97]
    },
    {
        "identifier": 'EVENT_2672_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_114']
    },
    {
        "identifier": 'EVENT_2672_set_130',
        "command": 'set',
        "args": [0x70a7, 98]
    },
    {
        "identifier": 'EVENT_2672_jmp_131',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_114']
    },
    {
        "identifier": 'EVENT_2672_set_132',
        "command": 'set',
        "args": [0x70a7, 107]
    },
    {
        "identifier": 'EVENT_2672_jmp_133',
        "command": 'jmp',
        "args": ['EVENT_2672_play_sound_114']
    },
    {
        "identifier": 'EVENT_2672_clear_bit_134',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_135',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2672_add_136',
        "command": 'add',
        "args": [0x70c9, 0x01]
    },
    {
        "identifier": 'EVENT_2672_jmp_if_bit_set_137',
        "command": 'jmp_if_bit_set',
        "args": [0x7099, 6, 'EVENT_2672_set_random_93']
    },
    {
        "identifier": 'EVENT_2672_set_bit_138',
        "command": 'set_bit',
        "args": [0x7099, 6]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_139',
        "command": 'run_dialog',
        "args": [38, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_set_140',
        "command": 'set',
        "args": [0x70a7, 174]
    },
    {
        "identifier": 'EVENT_2672_set_141',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2672_run_event_as_subroutine_142',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_2672_run_dialog_143',
        "command": 'run_dialog',
        "args": [39, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_144',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_145',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_146',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_147',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_148',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_149',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_150',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_2672_clear_bit_151',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_152',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_152_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_152_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_152_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [12, 255, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2672_action_queue_sync_153_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_153_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
            },
            {
                "identifier": 'EVENT_2672_action_queue_sync_153_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [244, 255, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2672_remember_last_object_154',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_2672_set_action_script_sync_155',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 892]
    },
    {
        "identifier": 'EVENT_2672_enable_trigger_156',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2672_ret_157',
        "command": 'ret'
    }
]
