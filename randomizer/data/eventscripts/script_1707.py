from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1707_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_1707_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1707_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1707_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1707_reset_coords_4',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_1707_reset_coords_5',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1707_reset_coords_6',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1707_reset_coords_7',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_jmp_if_bit_clear_4',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 7, 'EVENT_1707_clear_bit_9']
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_walk_1_step_east_7',
                "command": 'walk_1_step_east'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_8_SUBSCRIPT_shift_northeast_steps_8',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1707_set_random_10',
        "command": 'set_random',
        "args": [0x7000, 32768]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_7000_all_bits_clear_11',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[0], 'EVENT_1707_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1707_set_bit_12',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1707_mem_compare_14',
        "command": 'mem_compare',
        "args": [0x7000, 16384]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_comparison_result_is_lesser_15',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1707_mem_7000_and_const_17']
    },
    {
        "identifier": 'EVENT_1707_set_bit_16',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1707_mem_7000_and_const_17',
        "command": 'mem_7000_and_const',
        "args": [0x3fff]
    },
    {
        "identifier": 'EVENT_1707_mem_compare_18',
        "command": 'mem_compare',
        "args": [0x7000, 8192]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_comparison_result_is_lesser_19',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1707_jmp_if_bit_set_22']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1707_set_77']
    },
    {
        "identifier": 'EVENT_1707_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_1707_set_59']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1707_set_41']
    },
    {
        "identifier": 'EVENT_1707_set_23',
        "command": 'set',
        "args": [0x7000, 12288]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1707_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1707_action_queue_async_32']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1707_action_queue_async_30']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_1707_action_queue_async_28']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_28_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_34']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_30_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_30_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_30_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_30_SUBSCRIPT_shift_north_steps_3',
                "command": 'shift_north_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_34']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_32_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_32_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_32_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [9]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_34']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_34_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [11, 95, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_set_35',
        "command": 'set',
        "args": [0x70a9, 25]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_36',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_37',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1707_set_bit_39',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1707_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_sync_97']
    },
    {
        "identifier": 'EVENT_1707_set_41',
        "command": 'set',
        "args": [0x7000, 28672]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_42',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1707_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1707_action_queue_async_50']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1707_action_queue_async_48']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_1707_action_queue_async_46']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_46_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_46_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_46_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_52']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_48_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_49',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_52']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_50_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_50_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_50_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_52']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_52_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [15, 107, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_set_53',
        "command": 'set',
        "args": [0x70a9, 25]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_54',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_55',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1707_set_bit_57',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1707_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_sync_100']
    },
    {
        "identifier": 'EVENT_1707_set_59',
        "command": 'set',
        "args": [0x7000, 4096]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_60',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1707_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_61',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1707_action_queue_async_68']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_62',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1707_action_queue_async_66']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_63',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_1707_action_queue_async_64']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_64_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_64_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_64_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_70']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_66_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_67',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_70']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_68_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_68_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_68_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_68_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_70']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_70_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [11, 115, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_set_71',
        "command": 'set',
        "args": [0x70a9, 25]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_73',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_74',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1707_set_bit_75',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1707_jmp_76',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_sync_103']
    },
    {
        "identifier": 'EVENT_1707_set_77',
        "command": 'set',
        "args": [0x7000, 20480]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_78',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_1707_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_79',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1707_action_queue_async_86']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_80',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1707_action_queue_async_84']
    },
    {
        "identifier": 'EVENT_1707_jmp_if_bit_set_81',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1707_action_queue_async_82']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_82_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_82_SUBSCRIPT_walk_1_step_north_1',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_82_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [9]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_83',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_88']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_84',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_84_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_84_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_84_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_85',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_88']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_86_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_jmp_87',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_async_88']
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_88_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [7, 103, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_set_89',
        "command": 'set',
        "args": [0x70a9, 25]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_91',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1707_clear_bit_92',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1707_set_bit_93',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1707_action_queue_sync_94',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_sync_94_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x12]
            },
            {
                "identifier": 'EVENT_1707_action_queue_sync_94_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [10, 90, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_add_95',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_var_equals_byte_96',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 28, 'EVENT_1707_clear_bit_107']
    },
    {
        "identifier": 'EVENT_1707_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_sync_97_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x12]
            },
            {
                "identifier": 'EVENT_1707_action_queue_sync_97_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [14, 102, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_add_98',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_var_equals_byte_99',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 28, 'EVENT_1707_clear_bit_107']
    },
    {
        "identifier": 'EVENT_1707_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_sync_100_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x12]
            },
            {
                "identifier": 'EVENT_1707_action_queue_sync_100_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [10, 110, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_add_101',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_var_equals_byte_102',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 28, 'EVENT_1707_clear_bit_107']
    },
    {
        "identifier": 'EVENT_1707_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_sync_103_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x12]
            },
            {
                "identifier": 'EVENT_1707_action_queue_sync_103_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [6, 98, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_add_104',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_1707_jmp_if_var_equals_byte_105',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a9, 28, 'EVENT_1707_clear_bit_107']
    },
    {
        "identifier": 'EVENT_1707_jmp_106',
        "command": 'jmp',
        "args": ['EVENT_1707_action_queue_sync_94']
    },
    {
        "identifier": 'EVENT_1707_clear_bit_107',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1707_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 6, 'EVENT_1707_set_action_script_sync_109']
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_set_bit_3',
                "command": 'set_bit',
                "args": [0x7043, 7]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_walk_1_step_west_5',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_walk_1_step_northwest_6',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_walk_1_step_north_7',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_1707_action_queue_async_108_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1707_set_action_script_sync_109',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 472]
    },
    {
        "identifier": 'EVENT_1707_set_action_script_sync_110',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 472]
    },
    {
        "identifier": 'EVENT_1707_set_action_script_sync_111',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 472]
    },
    {
        "identifier": 'EVENT_1707_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 469]
    },
    {
        "identifier": 'EVENT_1707_ret_113',
        "command": 'ret'
    }
]
