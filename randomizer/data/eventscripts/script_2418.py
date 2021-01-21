from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2418_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 242, 'EVENT_2418_jmp_if_bit_set_8']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 236, 'EVENT_2418_action_queue_async_4']
    },
    {
        "identifier": 'EVENT_2418_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_2418_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_2418_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_async_4_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_4_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_4_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_async_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 947]
    },
    {
        "identifier": 'EVENT_2418_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_2418_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 7, 'EVENT_2418_remove_from_current_level_31']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 5, 'EVENT_2418_remove_from_current_level_44']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 6, 'EVENT_2418_remove_from_current_level_51']
    },
    {
        "identifier": 'EVENT_2418_apply_solidity_mod_11',
        "command": 'apply_solidity_mod',
        "args": [Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_15',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_16',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_17',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_18',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_19',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_random_above_128_20',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2418_jmp_if_random_above_128_22']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_random_above_128_22',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2418_jmp_if_random_above_128_24']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_23',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_random_above_128_24',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2418_jmp_if_random_above_128_26']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_random_above_128_26',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2418_jmp_if_random_above_128_28']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_27',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_random_above_128_28',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2418_jmp_30']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_2418_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_2418_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_33',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_34',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_35',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_36',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_37',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_38',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_39',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_object_not_in_level_40',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_13, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, 'EVENT_2418_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_2418_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_async_41_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_41_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_41_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_41_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_41_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_41_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_13, 947]
    },
    {
        "identifier": 'EVENT_2418_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_2418_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_44',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_45',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_46',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_47',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_48',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_49',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2418_jmp_50',
        "command": 'jmp',
        "args": ['EVENT_2418_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_51',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_52',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_53',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_54',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_55',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_56',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_57',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_58',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_59',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_60',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_2418_remove_from_current_level_61',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_clear_62',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 1, 'EVENT_2418_fade_in_from_black_async_120']
    },
    {
        "identifier": 'EVENT_2418_play_sound_63',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_2418_clear_bit_64',
        "command": 'clear_bit',
        "args": [0x7047, 1]
    },
    {
        "identifier": 'EVENT_2418_freeze_camera_65',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2418_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_async_66_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_66_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_66_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_66_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_fade_in_from_black_async_67',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2418_pause_68',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2418_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_async_69_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_69_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_69_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_69_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2418_action_queue_async_69_SUBSCRIPT_pause_2']
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_play_sound_70',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2418_set_7000_to_current_level_71',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_72',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 233, 'EVENT_2418_set_7000_to_object_coord_84']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_73',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 235, 'EVENT_2418_action_queue_sync_78']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_74',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 236, 'EVENT_2418_action_queue_sync_80']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_75',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 242, 'EVENT_2418_action_queue_sync_82']
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_76_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_76_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_jmp_77',
        "command": 'jmp',
        "args": ['EVENT_2418_action_queue_async_89']
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_78_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_2418_action_queue_async_89']
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_80_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_80_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_2418_action_queue_async_89']
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_82_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_jmp_83',
        "command": 'jmp',
        "args": ['EVENT_2418_action_queue_async_89']
    },
    {
        "identifier": 'EVENT_2418_set_7000_to_object_coord_84',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_85',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2418_action_queue_sync_88']
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_86_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_jmp_87',
        "command": 'jmp',
        "args": ['EVENT_2418_action_queue_async_89']
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_88',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_88_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_88_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_async_89_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_89_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_89_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_89_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2418_action_queue_async_89_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_action_queue_sync_90',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2418_action_queue_sync_90_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_90_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_90_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x0a]
            },
            {
                "identifier": 'EVENT_2418_action_queue_sync_90_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_2418_pause_91',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2418_set_action_script_async_92',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2418_unfreeze_camera_93',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2418_set_7000_to_current_level_94',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_2418_jmp_if_var_equals_short_95',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 242, 'EVENT_2418_run_event_as_subroutine_97']
    },
    {
        "identifier": 'EVENT_2418_ret_96',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2418_run_event_as_subroutine_97',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_clear_98',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2418_clear_bit_118']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_set_99',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 5, 'EVENT_2418_jmp_if_object_not_in_level_104']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_set_100',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 6, 'EVENT_2418_jmp_if_object_not_in_level_109']
    },
    {
        "identifier": 'EVENT_2418_jmp_if_bit_set_101',
        "command": 'jmp_if_bit_set',
        "args": [0x7046, 7, 'EVENT_2418_jmp_if_object_not_in_level_114']
    },
    {
        "identifier": 'EVENT_2418_clear_bit_102',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2418_ret_103',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2418_jmp_if_object_not_in_level_104',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, 'EVENT_2418_clear_bit_118']
    },
    {
        "identifier": 'EVENT_2418_pause_105',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2418_clear_bit_106',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2418_play_sound_107',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2418_ret_108',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2418_jmp_if_object_not_in_level_109',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_7, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, 'EVENT_2418_clear_bit_118']
    },
    {
        "identifier": 'EVENT_2418_pause_110',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2418_clear_bit_111',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2418_play_sound_112',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2418_ret_113',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2418_jmp_if_object_not_in_level_114',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, 'EVENT_2418_clear_bit_118']
    },
    {
        "identifier": 'EVENT_2418_pause_115',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2418_clear_bit_116',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2418_play_sound_117',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2418_clear_bit_118',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2418_ret_119',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2418_fade_in_from_black_async_120',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2418_clear_bit_121',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2418_ret_122',
        "command": 'ret'
    }
]
