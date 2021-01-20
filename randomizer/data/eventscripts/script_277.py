from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_277_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7032, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_7000_any_bits_set_2',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0], 'EVENT_277_jmp_if_var_equals_short_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_277_action_queue_async_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 1, 'EVENT_277_action_queue_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 3, 'EVENT_277_action_queue_async_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 5, 'EVENT_277_action_queue_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 7, 'EVENT_277_action_queue_async_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_277_action_queue_async_8_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x24, 0x00, 0x10]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_8_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x7000, 0x700c]
            }
        ]
    },
    {
        "identifier": 'EVENT_277_mem_7000_and_const_9',
        "command": 'mem_7000_and_const',
        "args": [0x00c0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_277_action_queue_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 64, 'EVENT_277_action_queue_async_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_277_action_queue_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 192, 'EVENT_277_action_queue_async_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_277_action_queue_async_14_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_14_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_14_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_277_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_277_action_queue_async_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_277_action_queue_async_16_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_16_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_16_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_16_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_277_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_277_action_queue_async_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_277_action_queue_async_18_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_18_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_18_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_18_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_18_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_277_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_277_action_queue_async_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_277_action_queue_async_20_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_20_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_20_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_20_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_277_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_277_action_queue_async_21_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_277_action_queue_async_21_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7032]
            },
            {
                "identifier": 'EVENT_277_action_queue_async_21_SUBSCRIPT_face_east_2',
                "command": 'face_east',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_277_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_277_ret_23',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
