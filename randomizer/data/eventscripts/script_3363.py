from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3363_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_async_0_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_0_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x7038, 0x700c]
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_3363_add_2',
        "command": 'add',
        "args": [0x7000, 65515]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_7000_any_bits_set_4',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_3363_jmp_if_7000_any_bits_set_12']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_7000_any_bits_set_5',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_3363_jmp_if_var_equals_short_9']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 7, 'EVENT_3363_set_short_mem_19']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 1, 'EVENT_3363_set_short_mem_35']
    },
    {
        "identifier": 'EVENT_3363_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 1, 'EVENT_3363_set_short_mem_35']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 3, 'EVENT_3363_set_short_mem_53']
    },
    {
        "identifier": 'EVENT_3363_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_3363_jmp_if_var_equals_short_16']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 5, 'EVENT_3363_set_short_mem_71']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 7, 'EVENT_3363_set_short_mem_19']
    },
    {
        "identifier": 'EVENT_3363_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 5, 'EVENT_3363_set_short_mem_71']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 3, 'EVENT_3363_set_short_mem_53']
    },
    {
        "identifier": 'EVENT_3363_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_20',
        "command": 'add',
        "args": [0x7000, 25]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_21',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_22',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_add_23',
        "command": 'add',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_25',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_set_short_mem_27']
    },
    {
        "identifier": 'EVENT_3363_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_27',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_28',
        "command": 'add',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_30',
        "command": 'add',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_32',
        "command": 'add',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_3363_clear_bit_89']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_36',
        "command": 'add',
        "args": [0x7000, 22]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_37',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_38',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_add_39',
        "command": 'add',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_40',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_41',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_set_short_mem_43']
    },
    {
        "identifier": 'EVENT_3363_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_43',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_44',
        "command": 'add',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_45',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_46',
        "command": 'add',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_47',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_48',
        "command": 'add',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_49',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_51',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3363_jmp_52',
        "command": 'jmp',
        "args": ['EVENT_3363_clear_bit_89']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_54',
        "command": 'add',
        "args": [0x7000, 17]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_55',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_56',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_add_57',
        "command": 'add',
        "args": [0x7000, 65532]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_58',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_59',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_set_short_mem_61']
    },
    {
        "identifier": 'EVENT_3363_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_61',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_62',
        "command": 'add',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_63',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_64',
        "command": 'add',
        "args": [0x7000, 65532]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_65',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_66',
        "command": 'add',
        "args": [0x7000, 65532]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_67',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_68',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_69',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3363_jmp_70',
        "command": 'jmp',
        "args": ['EVENT_3363_clear_bit_89']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_71',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_72',
        "command": 'add',
        "args": [0x7000, 20]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_73',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_74',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_add_75',
        "command": 'add',
        "args": [0x7000, 65535]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_76',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_77',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_set_short_mem_79']
    },
    {
        "identifier": 'EVENT_3363_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_3363_play_sound_153']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_79',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_80',
        "command": 'add',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_81',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_82',
        "command": 'add',
        "args": [0x7000, 65535]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_83',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_84',
        "command": 'add',
        "args": [0x7000, 65535]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_85',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_86',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_87',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3363_jmp_88',
        "command": 'jmp',
        "args": ['EVENT_3363_clear_bit_89']
    },
    {
        "identifier": 'EVENT_3363_clear_bit_89',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3363_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.F]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_if_var_equals_short_1',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 7, 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_5']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_7']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_9']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_11']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_8',
                "command": 'jmp',
                "args": ['EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_10',
                "command": 'jmp',
                "args": ['EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_jmp_12',
                "command": 'jmp',
                "args": ['EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_91_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_set_short_mem_0',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7038]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xc8, 0x07]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 4]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [124]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_shift_f_direction_steps_6',
                "command": 'shift_f_direction_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_set_bit_7',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_jump_to_height_silent_8',
                "command": 'jump_to_height_silent',
                "args": [120]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_shift_f_direction_steps_9',
                "command": 'shift_f_direction_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_set_bit_10',
                "command": 'set_bit',
                "args": [0x7043, 2]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_db_12',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_object_memory_set_bit_14',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_clear_solidity_bits_15',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_92_SUBSCRIPT_end_all_16',
                "command": 'end_all'
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_action_queue_sync_93',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 1, 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_object_memory_set_bit_4',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_clear_solidity_bits_5',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x57]
            },
            {
                "identifier": 'EVENT_3363_action_queue_sync_93_SUBSCRIPT_end_all_8',
                "command": 'end_all'
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_action_queue_async_94',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_async_94_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_94_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 2, 'EVENT_3363_action_queue_async_94_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_94_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_94_SUBSCRIPT_object_memory_clear_bit_3',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_94_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_94_SUBSCRIPT_end_all_5',
                "command": 'end_all'
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_dec_short_95',
        "command": 'dec_short',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_equals_short_96',
        "command": 'jmp_if_var_equals_short',
        "args": [0x703e, 1, 'EVENT_3363_pause_155']
    },
    {
        "identifier": 'EVENT_3363_jmp_97',
        "command": 'jmp',
        "args": ['EVENT_3363_clear_bit_98']
    },
    {
        "identifier": 'EVENT_3363_clear_bit_98',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3363_set_short_99',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_100',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_101',
        "command": 'add',
        "args": [0x7000, 21]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_102',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_103',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_add_short_149']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_104',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_7000_any_bits_set_105',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_3363_jmp_if_7000_any_bits_set_113']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_7000_any_bits_set_106',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_3363_jmp_to_subroutine_110']
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_107',
        "command": 'jmp_to_subroutine',
        "args": [0x5663]
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_108',
        "command": 'jmp_to_subroutine',
        "args": [0x5672]
    },
    {
        "identifier": 'EVENT_3363_jmp_109',
        "command": 'jmp',
        "args": ['EVENT_3363_add_short_149']
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_110',
        "command": 'jmp_to_subroutine',
        "args": [0x5672]
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_111',
        "command": 'jmp_to_subroutine',
        "args": [0x5681]
    },
    {
        "identifier": 'EVENT_3363_jmp_112',
        "command": 'jmp',
        "args": ['EVENT_3363_add_short_149']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_7000_any_bits_set_113',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_3363_jmp_to_subroutine_117']
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_114',
        "command": 'jmp_to_subroutine',
        "args": [0x5690]
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_115',
        "command": 'jmp_to_subroutine',
        "args": [0x5663]
    },
    {
        "identifier": 'EVENT_3363_jmp_116',
        "command": 'jmp',
        "args": ['EVENT_3363_add_short_149']
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_117',
        "command": 'jmp_to_subroutine',
        "args": [0x5690]
    },
    {
        "identifier": 'EVENT_3363_jmp_to_subroutine_118',
        "command": 'jmp_to_subroutine',
        "args": [0x5681]
    },
    {
        "identifier": 'EVENT_3363_jmp_119',
        "command": 'jmp',
        "args": ['EVENT_3363_add_short_149']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_120',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_121',
        "command": 'add',
        "args": [0x7000, 25]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_122',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_123',
        "command": 'add',
        "args": [0x7000, 4]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_124',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_125',
        "command": 'jmp',
        "args": ['EVENT_3363_jmp_if_present_in_current_level_144']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_126',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_127',
        "command": 'add',
        "args": [0x7000, 22]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_128',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_129',
        "command": 'add',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_130',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_131',
        "command": 'jmp',
        "args": ['EVENT_3363_jmp_if_present_in_current_level_144']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_132',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_133',
        "command": 'add',
        "args": [0x7000, 17]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_134',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_135',
        "command": 'add',
        "args": [0x7000, 65532]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_136',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_137',
        "command": 'jmp',
        "args": ['EVENT_3363_jmp_if_present_in_current_level_144']
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_138',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_3363_add_139',
        "command": 'add',
        "args": [0x7000, 20]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_140',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_add_141',
        "command": 'add',
        "args": [0x7000, 65535]
    },
    {
        "identifier": 'EVENT_3363_set_short_mem_142',
        "command": 'set_short_mem',
        "args": [0x70aa, 0x7000]
    },
    {
        "identifier": 'EVENT_3363_jmp_143',
        "command": 'jmp',
        "args": ['EVENT_3363_jmp_if_present_in_current_level_144']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_144',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70A9, 'EVENT_3363_ret_146']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_present_in_current_level_145',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70AA, 'EVENT_3363_set_bit_147']
    },
    {
        "identifier": 'EVENT_3363_ret_146',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3363_set_bit_147',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_3363_ret_148',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3363_add_short_149',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_3363_jmp_if_var_not_equals_short_150',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 16, 'EVENT_3363_set_short_mem_100']
    },
    {
        "identifier": 'EVENT_3363_jmp_if_bit_clear_151',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3363_play_sound_168']
    },
    {
        "identifier": 'EVENT_3363_ret_152',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3363_play_sound_153',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 4]
    },
    {
        "identifier": 'EVENT_3363_ret_154',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3363_pause_155',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_156',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3363_set_action_script_sync_157',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3363_play_sound_158',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 4]
    },
    {
        "identifier": 'EVENT_3363_pause_159',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3363_play_music_default_volume_160',
        "command": 'play_music_default_volume',
        "args": [Music._09_VICTORY]
    },
    {
        "identifier": 'EVENT_3363_run_dialog_161',
        "command": 'run_dialog',
        "args": [1914, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3363_set_bit_162',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3363_action_queue_async_163',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_163_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_play_sound_164',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3363_apply_tile_mod_165',
        "command": 'apply_tile_mod',
        "args": [Rooms._468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3363_apply_solidity_mod_166',
        "command": 'apply_solidity_mod',
        "args": [Rooms._468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3363_ret_167',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3363_play_sound_168',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 4]
    },
    {
        "identifier": 'EVENT_3363_pause_169',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3363_play_music_default_volume_170',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME]
    },
    {
        "identifier": 'EVENT_3363_slow_down_music_171',
        "command": 'slow_down_music'
    },
    {
        "identifier": 'EVENT_3363_action_queue_async_172',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3363_action_queue_async_172_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3363_action_queue_async_172_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3363_clear_bit_173',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3363_set_action_script_sync_174',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 59]
    },
    {
        "identifier": 'EVENT_3363_run_dialog_175',
        "command": 'run_dialog',
        "args": [1915, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3363_set_bit_176',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3363_pause_177',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_3363_fade_out_to_black_async_178',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3363_jmp_to_event_179',
        "command": 'jmp_to_event',
        "args": [3356]
    }
]
