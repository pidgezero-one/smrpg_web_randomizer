from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1846_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1846_clear_bit_30']
    },
    {
        "identifier": 'EVENT_1846_enable_controls_1',
        "command": 'enable_controls',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1846_move_script_to_background_thread_2_2',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1846_set_bit_3',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_1846_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F, []]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x702a, 0x700c]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0xc8, 0x91]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_run_away_shift_6',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_set_short_mem_9',
                "command": 'set_short_mem',
                "args": [0x700c, 0x702a]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_6_SUBSCRIPT_face_east_7C_10',
                "command": 'face_east_7C'
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_set_7000_to_tapped_button_7',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1846_jmp_if_7000_any_bits_set_8',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1846_action_queue_sync_21']
    },
    {
        "identifier": 'EVENT_1846_jmp_if_mario_in_air_9',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1846_clear_bit_30']
    },
    {
        "identifier": 'EVENT_1846_set_7000_to_pressed_button_10',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7010, 0x7000]
    },
    {
        "identifier": 'EVENT_1846_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 3], 'EVENT_1846_action_queue_sync_17']
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7010]
    },
    {
        "identifier": 'EVENT_1846_jmp_if_7000_any_bits_set_14',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 2], 'EVENT_1846_action_queue_sync_19']
    },
    {
        "identifier": 'EVENT_1846_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1846_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1846_set_7000_to_tapped_button_7']
    },
    {
        "identifier": 'EVENT_1846_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_sync_17_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_1846_pause_15']
    },
    {
        "identifier": 'EVENT_1846_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_sync_19_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_1846_pause_15']
    },
    {
        "identifier": 'EVENT_1846_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_sync_21_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_start_loop_n_times_22',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'EVENT_1846_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1846_set_7000_to_pressed_button_24',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x7010, 0x7000]
    },
    {
        "identifier": 'EVENT_1846_jmp_if_7000_any_bits_set_26',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 3], 'EVENT_1846_set_short_mem_33']
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_27',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7010]
    },
    {
        "identifier": 'EVENT_1846_jmp_if_7000_any_bits_set_28',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 2], 'EVENT_1846_action_queue_async_39']
    },
    {
        "identifier": 'EVENT_1846_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1846_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1846_move_script_to_main_thread_31',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1846_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1846_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1846_jmp_if_7000_equals_short_34',
        "command": 'jmp_if_7000_equals_short',
        "args": [23, 'EVENT_1846_action_queue_async_37']
    },
    {
        "identifier": 'EVENT_1846_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_async_35_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_35_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_35_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1846_clear_bit_30']
    },
    {
        "identifier": 'EVENT_1846_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_async_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_37_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_37_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_1846_clear_bit_30']
    },
    {
        "identifier": 'EVENT_1846_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1846_action_queue_async_39_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_39_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1846_action_queue_async_39_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1846_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_1846_clear_bit_30']
    }
]
