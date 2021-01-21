from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2402_enable_controls_0',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2402_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2402_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2402_jmp_if_mario_in_air_3',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2402_set_bit_43']
    },
    {
        "identifier": 'EVENT_2402_set_7000_to_tapped_button_4',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_5',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[6], 'EVENT_2402_action_queue_async_8']
    },
    {
        "identifier": 'EVENT_2402_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_2402_set_7000_to_pressed_button_9']
    },
    {
        "identifier": 'EVENT_2402_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_set_7000_to_pressed_button_9',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_10',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_2402_jmp_if_bit_set_33']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_11',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_2402_jmp_if_bit_set_38']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_2402_jmp_if_bit_set_38']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_13',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_2402_jmp_if_bit_set_33']
    },
    {
        "identifier": 'EVENT_2402_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2402_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2402_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2402_clear_bit_31']
    },
    {
        "identifier": 'EVENT_2402_set_7000_to_object_coord_17',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F]
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2402_action_queue_sync_29']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_19',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2402_action_queue_sync_29']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2402_action_queue_sync_29']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_21',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2402_action_queue_sync_29']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_22',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2402_action_queue_sync_27']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2402_action_queue_sync_27']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2402_action_queue_sync_27']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_25',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2402_action_queue_sync_27']
    },
    {
        "identifier": 'EVENT_2402_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2402_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_bit_set_33',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2402_clear_bit_35',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_37',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_clear_bit_39',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2402_set_bit_40',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_set_bit_43',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2402_clear_bit_44',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2402_clear_bit_45',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2402_set_7000_to_pressed_button_46',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_47',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1], 'EVENT_2402_action_queue_sync_67']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_48',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_2402_action_queue_sync_65']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_49',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[2], 'EVENT_2402_action_queue_sync_65']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_7000_any_bits_set_50',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[3], 'EVENT_2402_action_queue_sync_67']
    },
    {
        "identifier": 'EVENT_2402_set_7000_to_object_coord_51',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F]
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_52',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2402_action_queue_sync_61']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_53',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2402_action_queue_sync_61']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_54',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2402_action_queue_sync_61']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_55',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2402_action_queue_sync_61']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_56',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2402_action_queue_sync_63']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_57',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2402_action_queue_sync_63']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_58',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_2402_action_queue_sync_63']
    },
    {
        "identifier": 'EVENT_2402_jmp_if_var_equals_short_59',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_2402_action_queue_sync_63']
    },
    {
        "identifier": 'EVENT_2402_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_63_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_64',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_65_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_66',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    },
    {
        "identifier": 'EVENT_2402_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2402_action_queue_sync_67_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2402_jmp_68',
        "command": 'jmp',
        "args": ['EVENT_2402_pause_1']
    }
]
