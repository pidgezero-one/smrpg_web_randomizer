from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_529_db_0',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_529_close_dialog_1',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_529_fade_out_music_to_volume_2',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_3_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_3_SUBSCRIPT_object_memory_clear_bit_2',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_jmp_if_bit_set_1',
                "command": 'jmp_if_bit_set',
                "args": [0x7060, 0, 'EVENT_529_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_4']
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_jmp_3',
                "command": 'jmp',
                "args": ['EVENT_529_action_queue_sync_5']
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_4',
                "command": 'transfer_to_xyzf',
                "args": [12, 47, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_4_SUBSCRIPT_object_memory_clear_bit_6',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_5_SUBSCRIPT_object_memory_clear_bit_0',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_5_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7085, 1, 'EVENT_529_action_queue_sync_6']
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_5_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_6_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_7_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_8_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 1, 'EVENT_529_jmp_if_bit_clear_14']
    },
    {
        "identifier": 'EVENT_529_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_10_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_11_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [240, 8, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_11_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_11_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 637]
    },
    {
        "identifier": 'EVENT_529_set_bit_13',
        "command": 'set_bit',
        "args": [0x7085, 1]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_clear_14',
        "command": 'jmp_if_bit_clear',
        "args": [0x7060, 4, 'EVENT_529_jmp_if_bit_set_177']
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 0, 'EVENT_529_jmp_if_bit_set_177']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_not_in_level_16',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 'EVENT_529_jmp_if_bit_set_177']
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 2, 'EVENT_529_set_bit_21']
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_18_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 21]
    },
    {
        "identifier": 'EVENT_529_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_529_clear_bit_23']
    },
    {
        "identifier": 'EVENT_529_set_bit_21',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_529_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_529_set_short_mem_181']
    },
    {
        "identifier": 'EVENT_529_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_529_run_background_event_24',
        "command": 'run_background_event',
        "args": [530, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_529_run_background_event_25',
        "command": 'run_background_event',
        "args": [551, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_529_set_26',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_529_pause_action_script_27',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'EVENT_529_start_embedded_action_script_async_28',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_start_embedded_action_script_async_28_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 28, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_529_start_embedded_action_script_async_28_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_fade_in_from_black_sync_29',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_30_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_30_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_pause_script_until_effect_done_31',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_529_remember_last_object_32',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_529_run_dialog_33',
        "command": 'run_dialog',
        "args": [792, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_jmp_if_dialog_option_b_34',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_529_pause_85']
    },
    {
        "identifier": 'EVENT_529_pause_35',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_event_as_subroutine_36',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_529_set_action_script_async_37',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_529_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_39',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_529_jmp_if_object_trigger_disabled_43']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_40',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_529_run_dialog_75']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_41',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_529_run_dialog_75']
    },
    {
        "identifier": 'EVENT_529_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_529_run_dialog_45']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_43',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F, 'EVENT_529_run_dialog_75']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_44',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F, 'EVENT_529_run_dialog_75']
    },
    {
        "identifier": 'EVENT_529_run_dialog_45',
        "command": 'run_dialog',
        "args": [794, AreaObjects.MEM_70A9, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_run_dialog_46',
        "command": 'run_dialog',
        "args": [799, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_47',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 2, 'EVENT_529_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_529_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7060, 5]
    },
    {
        "identifier": 'EVENT_529_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x7060, 6]
    },
    {
        "identifier": 'EVENT_529_set_bit_50',
        "command": 'set_bit',
        "args": [0x7060, 7]
    },
    {
        "identifier": 'EVENT_529_set_bit_51',
        "command": 'set_bit',
        "args": [0x7061, 0]
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_52',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_jmp_if_bit_set_160']
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_53',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_574_summon_to_level_0']
    },
    {
        "identifier": 'EVENT_529_summon_to_level_54',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_summon_to_level_55',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_remove_from_level_56',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_529_ret_57',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_58_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_58_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_58_SUBSCRIPT_shift_z_down_steps_2',
                "command": 'shift_z_down_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_58_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_run_dialog_59',
        "command": 'run_dialog',
        "args": [806, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_add_frog_coins_60',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_529_play_sound_61',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_529_set_bit_62',
        "command": 'set_bit',
        "args": [0x705d, 2]
    },
    {
        "identifier": 'EVENT_529_run_dialog_63',
        "command": 'run_dialog',
        "args": [2243, AreaObjects.BOWSER, []]
    },
    {
        "identifier": 'EVENT_529_set_7000_to_object_coord_64',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A9, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_529_mem_compare_65',
        "command": 'mem_compare',
        "args": [0x7000, 26]
    },
    {
        "identifier": 'EVENT_529_jmp_if_comparison_result_is_lesser_66',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_529_jmp_to_subroutine_73']
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_67',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_action_queue_async_159']
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_68',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_574_summon_to_level_0']
    },
    {
        "identifier": 'EVENT_529_summon_to_level_69',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_summon_to_level_70',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_remove_from_level_71',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_529_ret_72',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_73',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_action_queue_async_171']
    },
    {
        "identifier": 'EVENT_529_jmp_74',
        "command": 'jmp',
        "args": ['EVENT_529_jmp_if_bit_set_68']
    },
    {
        "identifier": 'EVENT_529_run_dialog_75',
        "command": 'run_dialog',
        "args": [794, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_76',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_action_queue_async_159']
    },
    {
        "identifier": 'EVENT_529_set_bit_77',
        "command": 'set_bit',
        "args": [0x7060, 5]
    },
    {
        "identifier": 'EVENT_529_clear_bit_78',
        "command": 'clear_bit',
        "args": [0x7060, 6]
    },
    {
        "identifier": 'EVENT_529_clear_bit_79',
        "command": 'clear_bit',
        "args": [0x7060, 7]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_80',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_574_summon_to_level_0']
    },
    {
        "identifier": 'EVENT_529_summon_to_level_81',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_summon_to_level_82',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_remove_from_level_83',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_529_ret_84',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_pause_85',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_set_action_script_async_86',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_529_remember_last_object_87',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_529_pause_88',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_dialog_89',
        "command": 'run_dialog',
        "args": [796, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_90',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_90_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_90_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_90_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_91',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_91_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_92',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_529_apply_tile_mod_97']
    },
    {
        "identifier": 'EVENT_529_apply_tile_mod_93',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 1, []]
    },
    {
        "identifier": 'EVENT_529_apply_solidity_mod_94',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 2, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_529_play_sound_95',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_529_jmp_96',
        "command": 'jmp',
        "args": ['EVENT_529_action_queue_async_100']
    },
    {
        "identifier": 'EVENT_529_apply_tile_mod_97',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 1, []]
    },
    {
        "identifier": 'EVENT_529_apply_solidity_mod_98',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 2, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_529_play_sound_99',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_100',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_100_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_100_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_100_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_pause_101',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_102_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_102_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_102_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_102_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_102_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_103',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_529_jmp_if_object_trigger_disabled_107']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_104',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_529_pause_126']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_105',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, 'EVENT_529_pause_126']
    },
    {
        "identifier": 'EVENT_529_jmp_106',
        "command": 'jmp',
        "args": ['EVENT_529_pause_109']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_107',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_1, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F, 'EVENT_529_pause_126']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_trigger_disabled_108',
        "command": 'jmp_if_object_trigger_disabled',
        "args": [AreaObjects.NPC_0, Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F, 'EVENT_529_pause_126']
    },
    {
        "identifier": 'EVENT_529_pause_109',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_dialog_110',
        "command": 'run_dialog',
        "args": [797, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_pause_111',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_112',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [26, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_112_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_pause_113',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_dialog_114',
        "command": 'run_dialog',
        "args": [798, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_115',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 2, 'EVENT_529_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_116',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_action_queue_async_171']
    },
    {
        "identifier": 'EVENT_529_set_bit_117',
        "command": 'set_bit',
        "args": [0x7060, 6]
    },
    {
        "identifier": 'EVENT_529_clear_bit_118',
        "command": 'clear_bit',
        "args": [0x7060, 5]
    },
    {
        "identifier": 'EVENT_529_clear_bit_119',
        "command": 'clear_bit',
        "args": [0x7060, 7]
    },
    {
        "identifier": 'EVENT_529_set_bit_120',
        "command": 'set_bit',
        "args": [0x7061, 0]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_121',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_574_summon_to_level_0']
    },
    {
        "identifier": 'EVENT_529_summon_to_level_122',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_summon_to_level_123',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_remove_from_level_124',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_529_ret_125',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_pause_126',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_dialog_127',
        "command": 'run_dialog',
        "args": [795, AreaObjects.MEM_70A9, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_jmp_if_dialog_option_b_128',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_529_pause_144']
    },
    {
        "identifier": 'EVENT_529_pause_129',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_130',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_130_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_130_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_130_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_pause_131',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_dialog_132',
        "command": 'run_dialog',
        "args": [798, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_133',
        "command": 'jmp_if_bit_set',
        "args": [0x7047, 2, 'EVENT_529_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_134',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_action_queue_async_171']
    },
    {
        "identifier": 'EVENT_529_set_bit_135',
        "command": 'set_bit',
        "args": [0x7060, 6]
    },
    {
        "identifier": 'EVENT_529_clear_bit_136',
        "command": 'clear_bit',
        "args": [0x7060, 5]
    },
    {
        "identifier": 'EVENT_529_clear_bit_137',
        "command": 'clear_bit',
        "args": [0x7060, 7]
    },
    {
        "identifier": 'EVENT_529_set_bit_138',
        "command": 'set_bit',
        "args": [0x7061, 0]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_139',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_574_summon_to_level_0']
    },
    {
        "identifier": 'EVENT_529_summon_to_level_140',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_summon_to_level_141',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_remove_from_level_142',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_529_ret_143',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_pause_144',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_set_action_script_async_145',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_529_remember_last_object_146',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_529_pause_147',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_run_dialog_148',
        "command": 'run_dialog',
        "args": [804, AreaObjects.MEM_70A9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_149',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_149_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_to_subroutine_150',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_529_action_queue_async_171']
    },
    {
        "identifier": 'EVENT_529_set_bit_151',
        "command": 'set_bit',
        "args": [0x7060, 5]
    },
    {
        "identifier": 'EVENT_529_clear_bit_152',
        "command": 'clear_bit',
        "args": [0x7060, 6]
    },
    {
        "identifier": 'EVENT_529_clear_bit_153',
        "command": 'clear_bit',
        "args": [0x7060, 7]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_154',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_574_summon_to_level_0']
    },
    {
        "identifier": 'EVENT_529_summon_to_level_155',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_summon_to_level_156',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F]
    },
    {
        "identifier": 'EVENT_529_remove_from_level_157',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F]
    },
    {
        "identifier": 'EVENT_529_ret_158',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_action_queue_async_159',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_159_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_159_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_159_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_160',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_529_apply_tile_mod_165']
    },
    {
        "identifier": 'EVENT_529_apply_tile_mod_161',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 1, []]
    },
    {
        "identifier": 'EVENT_529_apply_solidity_mod_162',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 2, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_529_play_sound_163',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_529_jmp_164',
        "command": 'jmp',
        "args": ['EVENT_529_jmp_if_bit_set_172']
    },
    {
        "identifier": 'EVENT_529_apply_tile_mod_165',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 1, []]
    },
    {
        "identifier": 'EVENT_529_apply_solidity_mod_166',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 2, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_529_play_sound_167',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_529_pause_168',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_529_remove_from_current_level_169',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_529_remove_from_current_level_170',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_171',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_171_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_172',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 4, 'EVENT_529_remove_from_current_level_170']
    },
    {
        "identifier": 'EVENT_529_remove_from_level_173',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE]
    },
    {
        "identifier": 'EVENT_529_ret_174',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_remove_from_level_175',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._084_ROSE_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_529_ret_176',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_177',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 2, 'EVENT_529_set_short_mem_181']
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_178',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_178_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_set_action_script_sync_179',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 21]
    },
    {
        "identifier": 'EVENT_529_jmp_180',
        "command": 'jmp',
        "args": ['EVENT_529_jmp_if_bit_set_194']
    },
    {
        "identifier": 'EVENT_529_set_short_mem_181',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_529_jmp_if_7000_any_bits_set_182',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_529_set_short_mem_190']
    },
    {
        "identifier": 'EVENT_529_set_short_mem_183',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7000]
    },
    {
        "identifier": 'EVENT_529_set_short_mem_184',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b9]
    },
    {
        "identifier": 'EVENT_529_set_short_mem_185',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7000]
    },
    {
        "identifier": 'EVENT_529_set_short_186',
        "command": 'set_short',
        "args": [0x701a, 0x0002]
    },
    {
        "identifier": 'EVENT_529_action_queue_async_187',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_object_memory_clear_bit_0',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x9a]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_jmp_if_bit_set_2',
                "command": 'jmp_if_bit_set',
                "args": [0x7043, 2, 'EVENT_529_action_queue_async_187_SUBSCRIPT_set_sprite_sequence_6']
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [240, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_529_action_queue_async_187_SUBSCRIPT_fixed_f_coord_on_8']
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_transfer_xyzf_pixels_7',
                "command": 'transfer_xyzf_pixels',
                "args": [16, 8, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_529_action_queue_async_187_SUBSCRIPT_fixed_f_coord_on_8',
                "command": 'fixed_f_coord_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_188',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_529_clear_bit_23']
    },
    {
        "identifier": 'EVENT_529_jmp_189',
        "command": 'jmp',
        "args": ['EVENT_529_jmp_if_bit_set_194']
    },
    {
        "identifier": 'EVENT_529_set_short_mem_190',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_529_mem_7000_and_const_191',
        "command": 'mem_7000_and_const',
        "args": [0x007f]
    },
    {
        "identifier": 'EVENT_529_set_bit_192',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_529_jmp_193',
        "command": 'jmp',
        "args": ['EVENT_529_set_short_mem_183']
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_194',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 0, 'EVENT_529_jmp_212']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_not_in_level_195',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 'EVENT_529_fade_in_from_black_async_197']
    },
    {
        "identifier": 'EVENT_529_set_action_script_sync_196',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 98]
    },
    {
        "identifier": 'EVENT_529_fade_in_from_black_async_197',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_198',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 4, 'EVENT_529_run_background_event_207']
    },
    {
        "identifier": 'EVENT_529_jmp_if_object_in_level_199',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_1, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 'EVENT_529_run_background_event_207']
    },
    {
        "identifier": 'EVENT_529_set_bit_200',
        "command": 'set_bit',
        "args": [0x7060, 4]
    },
    {
        "identifier": 'EVENT_529_action_queue_sync_201',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_529_action_queue_sync_201_SUBSCRIPT_shift_north_pixels_9',
                "command": 'shift_north_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_529_pause_202',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_529_apply_tile_mod_203',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_529_apply_solidity_mod_204',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_529_play_sound_205',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_529_remember_last_object_206',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_529_run_background_event_207',
        "command": 'run_background_event',
        "args": [530, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_529_run_background_event_208',
        "command": 'run_background_event',
        "args": [551, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_529_jmp_if_bit_set_209',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_529_pause_210',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_529_ret_211',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_529_jmp_212',
        "command": 'jmp',
        "args": ['EVENT_529_fade_in_from_black_async_197']
    }
]
