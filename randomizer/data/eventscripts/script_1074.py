from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1074_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_1074_unfreeze_camera_1',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1074_stop_music_2',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1074_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_face_southwest_10',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [3, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_set_vram_priority_12',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_13',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_3_SUBSCRIPT_ret_14',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_pause_5',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_sync_6_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_9',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_193']
    },
    {
        "identifier": 'EVENT_1074_pause_10',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_12',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_215']
    },
    {
        "identifier": 'EVENT_1074_pause_14',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_16',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_237']
    },
    {
        "identifier": 'EVENT_1074_pause_18',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_20',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_21',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_259']
    },
    {
        "identifier": 'EVENT_1074_pause_22',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_24',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_25',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_281']
    },
    {
        "identifier": 'EVENT_1074_pause_26',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_27',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_28',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_29',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_303']
    },
    {
        "identifier": 'EVENT_1074_pause_30',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_31',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_32',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_33',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_325']
    },
    {
        "identifier": 'EVENT_1074_pause_34',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_set_short_mem_35',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7032]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_36',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_var_equals_short_369']
    },
    {
        "identifier": 'EVENT_1074_jmp_to_subroutine_37',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1074_jmp_if_bit_set_347']
    },
    {
        "identifier": 'EVENT_1074_pause_38',
        "command": 'pause',
        "args": [35]
    },
    {
        "identifier": 'EVENT_1074_pause_39',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1074_play_music_current_volume_40',
        "command": 'play_music_current_volume',
        "args": [Music._17_TADPOLE_POND]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_41',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_action_queue_async_190']
    },
    {
        "identifier": 'EVENT_1074_set_42',
        "command": 'set',
        "args": [0x7000, 0]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 6, 'EVENT_1078_set_short_mem_0']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_80']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_45',
        "command": 'jmp_if_bit_set',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_63']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_46',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 1, 'EVENT_1074_jmp_if_var_not_equals_short_48']
    },
    {
        "identifier": 'EVENT_1074_add_47',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_48',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 2, 'EVENT_1074_jmp_if_var_not_equals_short_50']
    },
    {
        "identifier": 'EVENT_1074_add_49',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_50',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 6, 'EVENT_1074_jmp_if_var_not_equals_short_52']
    },
    {
        "identifier": 'EVENT_1074_add_51',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_52',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 5, 'EVENT_1074_jmp_if_var_not_equals_short_54']
    },
    {
        "identifier": 'EVENT_1074_add_53',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_54',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 4, 'EVENT_1074_jmp_if_var_not_equals_short_56']
    },
    {
        "identifier": 'EVENT_1074_add_55',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_56',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 5, 'EVENT_1074_jmp_if_var_not_equals_short_58']
    },
    {
        "identifier": 'EVENT_1074_add_57',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_58',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 4, 'EVENT_1074_jmp_if_var_not_equals_short_60']
    },
    {
        "identifier": 'EVENT_1074_add_59',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_60',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 5, 'EVENT_1074_jmp_if_var_equals_short_97']
    },
    {
        "identifier": 'EVENT_1074_add_61',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_1074_jmp_if_var_equals_short_97']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_63',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 6, 'EVENT_1074_jmp_if_var_not_equals_short_65']
    },
    {
        "identifier": 'EVENT_1074_add_64',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_65',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 4, 'EVENT_1074_jmp_if_var_not_equals_short_67']
    },
    {
        "identifier": 'EVENT_1074_add_66',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_67',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 1, 'EVENT_1074_jmp_if_var_not_equals_short_69']
    },
    {
        "identifier": 'EVENT_1074_add_68',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_69',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 4, 'EVENT_1074_jmp_if_var_not_equals_short_71']
    },
    {
        "identifier": 'EVENT_1074_add_70',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_71',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 5, 'EVENT_1074_jmp_if_var_not_equals_short_73']
    },
    {
        "identifier": 'EVENT_1074_add_72',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_73',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 2, 'EVENT_1074_jmp_if_var_not_equals_short_75']
    },
    {
        "identifier": 'EVENT_1074_add_74',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_75',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 3, 'EVENT_1074_jmp_if_var_not_equals_short_77']
    },
    {
        "identifier": 'EVENT_1074_add_76',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_77',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 4, 'EVENT_1074_jmp_if_var_equals_short_97']
    },
    {
        "identifier": 'EVENT_1074_add_78',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_1074_jmp_if_var_equals_short_97']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_80',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 2, 'EVENT_1074_jmp_if_var_not_equals_short_82']
    },
    {
        "identifier": 'EVENT_1074_add_81',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_82',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 3, 'EVENT_1074_jmp_if_var_not_equals_short_84']
    },
    {
        "identifier": 'EVENT_1074_add_83',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_84',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 4, 'EVENT_1074_jmp_if_var_not_equals_short_86']
    },
    {
        "identifier": 'EVENT_1074_add_85',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_86',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 5, 'EVENT_1074_jmp_if_var_not_equals_short_88']
    },
    {
        "identifier": 'EVENT_1074_add_87',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_88',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 1, 'EVENT_1074_jmp_if_var_not_equals_short_90']
    },
    {
        "identifier": 'EVENT_1074_add_89',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_90',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 4, 'EVENT_1074_jmp_if_var_not_equals_short_92']
    },
    {
        "identifier": 'EVENT_1074_add_91',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_92',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 5, 'EVENT_1074_jmp_if_var_not_equals_short_94']
    },
    {
        "identifier": 'EVENT_1074_add_93',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_94',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 6, 'EVENT_1074_jmp_if_var_equals_short_97']
    },
    {
        "identifier": 'EVENT_1074_add_95',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1074_jmp_96',
        "command": 'jmp',
        "args": ['EVENT_1074_jmp_if_var_equals_short_97']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_97',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1074_pause_107']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_98',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1074_pause_113']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_99',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_1074_pause_113']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_100',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_1074_pause_121']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_101',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_1074_pause_121']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_102',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_1074_pause_129']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_103',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1074_pause_129']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_104',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_1074_pause_137']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_105',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 8, 'EVENT_1074_pause_145']
    },
    {
        "identifier": 'EVENT_1074_ret_106',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_pause_107',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_108',
        "command": 'run_dialog',
        "args": [2724, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_109',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_109_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_109_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_109_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_109_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_109_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_110',
        "command": 'run_dialog',
        "args": [2725, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_111',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_112',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_pause_113',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_114',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_114_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_114_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_115',
        "command": 'run_dialog',
        "args": [2724, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_116',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_116_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_116_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_116_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_116_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_116_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_117',
        "command": 'run_dialog',
        "args": [2726, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_119',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_120',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_pause_121',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_122',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_122_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_122_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_122_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_122_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_123',
        "command": 'run_dialog',
        "args": [2724, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_124',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_124_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_124_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_124_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_124_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_124_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_125',
        "command": 'run_dialog',
        "args": [2727, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_126_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_126_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_127',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_128',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_pause_129',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_130',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_130_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_131',
        "command": 'run_dialog',
        "args": [2724, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_132',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_132_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_132_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_132_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_132_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_132_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_133',
        "command": 'run_dialog',
        "args": [2728, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_134',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_134_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_134_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_135',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_136',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_pause_137',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_138',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_138_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_138_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_138_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_138_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_138_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_138_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_139',
        "command": 'run_dialog',
        "args": [2724, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_140',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_140_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_140_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_140_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_140_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_140_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_run_dialog_141',
        "command": 'run_dialog',
        "args": [2729, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_142',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_142_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_142_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_143',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_144',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_pause_145',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_146',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_146_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_pause_147',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_148',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_148_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_148_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_148_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_148_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_pause_149',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_150',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_150_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_150_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_pause_151',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_152',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_152_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_jmp_to_event_153',
        "command": 'jmp_to_event',
        "args": [560]
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_154',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_set_157']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_155',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_set_162']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_156',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_set_168']
    },
    {
        "identifier": 'EVENT_1074_set_157',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1074_run_event_as_subroutine_158',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1074_pause_159',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1074_set_bit_160',
        "command": 'set_bit',
        "args": [0x7051, 4]
    },
    {
        "identifier": 'EVENT_1074_jmp_161',
        "command": 'jmp',
        "args": ['EVENT_1074_action_queue_async_185']
    },
    {
        "identifier": 'EVENT_1074_set_162',
        "command": 'set',
        "args": [0x70a7, 152]
    },
    {
        "identifier": 'EVENT_1074_set_163',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1074_run_event_as_subroutine_164',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1074_pause_165',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1074_set_bit_166',
        "command": 'set_bit',
        "args": [0x7054, 5]
    },
    {
        "identifier": 'EVENT_1074_jmp_167',
        "command": 'jmp',
        "args": ['EVENT_1074_action_queue_async_185']
    },
    {
        "identifier": 'EVENT_1074_set_168',
        "command": 'set',
        "args": [0x70a7, 150]
    },
    {
        "identifier": 'EVENT_1074_set_169',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_1074_run_event_as_subroutine_170',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_1074_pause_171',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1074_set_bit_172',
        "command": 'set_bit',
        "args": [0x7054, 6]
    },
    {
        "identifier": 'EVENT_1074_set_bit_173',
        "command": 'set_bit',
        "args": [0x7093, 0]
    },
    {
        "identifier": 'EVENT_1074_jmp_174',
        "command": 'jmp',
        "args": ['EVENT_1074_action_queue_async_185']
    },
    {
        "identifier": 'EVENT_1074_stop_sound_175',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_176',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_177',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_178',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_179',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_180',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_181',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_182',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_stop_sound_183',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1074_run_dialog_184',
        "command": 'run_dialog',
        "args": [2734, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_185',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_185_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_remove_from_current_level_186',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1074_set_bit_187',
        "command": 'set_bit',
        "args": [0x7052, 1]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_188',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_189',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_action_queue_async_190',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1074_action_queue_async_190_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_190_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_190_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_190_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1074_action_queue_async_190_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1074_set_action_script_async_191',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1074_ret_192',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_193',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_212']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_194',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_200']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_195',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_204']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_196',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_208']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_197',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_198',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1074_ret_199',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_200',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 1, 'EVENT_1074_set_action_script_sync_212']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_201',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_202',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1074_ret_203',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_204',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 6, 'EVENT_1074_set_action_script_sync_212']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_205',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_206',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1074_ret_207',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_208',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 2, 'EVENT_1074_set_action_script_sync_212']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_209',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_210',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1074_ret_211',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_212',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_213',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1074_ret_214',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_215',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_234']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_216',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_222']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_217',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_226']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_218',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_230']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_219',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_220',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1074_ret_221',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_222',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 2, 'EVENT_1074_set_action_script_sync_234']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_223',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_224',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1074_ret_225',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_226',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 4, 'EVENT_1074_set_action_script_sync_234']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_227',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_228',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1074_ret_229',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_230',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 3, 'EVENT_1074_set_action_script_sync_234']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_231',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_232',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1074_ret_233',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_234',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_235',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1074_ret_236',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_237',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_256']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_238',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_244']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_239',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_248']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_240',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_252']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_241',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_242',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1074_ret_243',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_244',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 6, 'EVENT_1074_set_action_script_sync_256']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_245',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_246',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1074_ret_247',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_248',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 1, 'EVENT_1074_set_action_script_sync_256']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_249',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_250',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1074_ret_251',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_252',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 4, 'EVENT_1074_set_action_script_sync_256']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_253',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_254',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1074_ret_255',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_256',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_257',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1074_ret_258',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_259',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_278']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_260',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_266']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_261',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_270']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_262',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_274']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_263',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_264',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1074_ret_265',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_266',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 5, 'EVENT_1074_set_action_script_sync_278']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_267',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_268',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1074_ret_269',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_270',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 4, 'EVENT_1074_set_action_script_sync_278']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_271',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_272',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1074_ret_273',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_274',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702a, 5, 'EVENT_1074_set_action_script_sync_278']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_275',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_276',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1074_ret_277',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_278',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_279',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1074_ret_280',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_281',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_300']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_282',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_288']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_283',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_292']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_284',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_296']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_285',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_286',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1074_ret_287',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_288',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 4, 'EVENT_1074_set_action_script_sync_300']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_289',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_290',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1074_ret_291',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_292',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 5, 'EVENT_1074_set_action_script_sync_300']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_293',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_294',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1074_ret_295',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_296',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 1, 'EVENT_1074_set_action_script_sync_300']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_297',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_298',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1074_ret_299',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_300',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_301',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1074_ret_302',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_303',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_322']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_304',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_310']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_305',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_314']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_306',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_318']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_307',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_308',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1074_ret_309',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_310',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 5, 'EVENT_1074_set_action_script_sync_322']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_311',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_312',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1074_ret_313',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_314',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 2, 'EVENT_1074_set_action_script_sync_322']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_315',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_316',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1074_ret_317',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_318',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 4, 'EVENT_1074_set_action_script_sync_322']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_319',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_320',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1074_ret_321',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_322',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_323',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1074_ret_324',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_325',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_344']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_326',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_332']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_327',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_336']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_328',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_340']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_329',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_330',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_331',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_332',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 4, 'EVENT_1074_set_action_script_sync_344']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_333',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_334',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_335',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_336',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 3, 'EVENT_1074_set_action_script_sync_344']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_337',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_338',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_339',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_340',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7030, 5, 'EVENT_1074_set_action_script_sync_344']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_341',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_342',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_343',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_344',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_345',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_346',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_set_347',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 1, 'EVENT_1074_set_action_script_sync_366']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_348',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 4, 'EVENT_1074_jmp_if_var_not_equals_short_354']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_349',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 5, 'EVENT_1074_jmp_if_var_not_equals_short_358']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_bit_clear_350',
        "command": 'jmp_if_bit_clear',
        "args": [0x7054, 6, 'EVENT_1074_jmp_if_var_not_equals_short_362']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_351',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_352',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1074_ret_353',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_354',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 5, 'EVENT_1074_set_action_script_sync_366']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_355',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_356',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1074_ret_357',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_358',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 4, 'EVENT_1074_set_action_script_sync_366']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_359',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_360',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1074_ret_361',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_not_equals_short_362',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7032, 6, 'EVENT_1074_set_action_script_sync_366']
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_363',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 571]
    },
    {
        "identifier": 'EVENT_1074_set_bit_364',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1074_ret_365',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_set_action_script_sync_366',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 572]
    },
    {
        "identifier": 'EVENT_1074_clear_bit_367',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1074_ret_368',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_369',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1074_play_sound_376']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_370',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1074_play_sound_378']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_371',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_1074_play_sound_380']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_372',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_1074_play_sound_382']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_373',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_1074_play_sound_384']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_374',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_1074_play_sound_386']
    },
    {
        "identifier": 'EVENT_1074_jmp_if_var_equals_short_375',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1074_play_sound_388']
    },
    {
        "identifier": 'EVENT_1074_play_sound_376',
        "command": 'play_sound',
        "args": [Sounds._036_TADPOLE_POND_STAFF_DO, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_377',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_play_sound_378',
        "command": 'play_sound',
        "args": [Sounds._037_TADPOLE_POND_STAFF_RE, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_379',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_play_sound_380',
        "command": 'play_sound',
        "args": [Sounds._038_TADPOLE_POND_STAFF_MI, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_381',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_play_sound_382',
        "command": 'play_sound',
        "args": [Sounds._039_TADPOLE_POND_STAFF_FA, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_383',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_play_sound_384',
        "command": 'play_sound',
        "args": [Sounds._040_TADPOLE_POND_STAFF_SO, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_385',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_play_sound_386',
        "command": 'play_sound',
        "args": [Sounds._041_TADPOLE_POND_STAFF_LA, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_387',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1074_play_sound_388',
        "command": 'play_sound',
        "args": [Sounds._042_TADPOLE_POND_STAFF_TI, 6]
    },
    {
        "identifier": 'EVENT_1074_ret_389',
        "command": 'ret'
    }
]
