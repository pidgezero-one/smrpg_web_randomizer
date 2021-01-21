from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1537_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7095, 0, 'EVENT_1537_set_bit_2']
    },
    {
        "identifier": 'EVENT_1537_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1537_set_bit_2',
        "command": 'set_bit',
        "args": [0x7095, 0]
    },
    {
        "identifier": 'EVENT_1537_move_script_to_background_thread_2_3',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1537_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7018]
    },
    {
        "identifier": 'EVENT_1537_mem_7000_shift_left_5',
        "command": 'mem_7000_shift_left',
        "args": [0x7016, 8]
    },
    {
        "identifier": 'EVENT_1537_set_action_script_async_6',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 781]
    },
    {
        "identifier": 'EVENT_1537_set_7',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'EVENT_1537_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._031_SPINNING_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_1537_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1537_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1537_set_7000_to_tapped_button_11',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1537_jmp_if_7000_any_bits_set_12',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1537_set_action_script_async_18']
    },
    {
        "identifier": 'EVENT_1537_end_loop_13',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1537_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1537_action_queue_sync_14_SUBSCRIPT_turn_clockwise_45_degrees_n_times_0',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1537_add_15',
        "command": 'add',
        "args": [0x70ae, 0x01]
    },
    {
        "identifier": 'EVENT_1537_jmp_if_var_equals_byte_16',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 40, 'EVENT_1537_set_action_script_sync_23']
    },
    {
        "identifier": 'EVENT_1537_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_1537_play_sound_8']
    },
    {
        "identifier": 'EVENT_1537_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 820]
    },
    {
        "identifier": 'EVENT_1537_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7095, 0]
    },
    {
        "identifier": 'EVENT_1537_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7096, 6]
    },
    {
        "identifier": 'EVENT_1537_move_script_to_main_thread_21',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1537_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1537_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 165]
    },
    {
        "identifier": 'EVENT_1537_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1537_action_queue_async_24_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_24_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_24_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1537_pause_25',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_1537_jmp_if_objects_action_script_running_26',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.MARIO, 'EVENT_1537_action_queue_async_24']
    },
    {
        "identifier": 'EVENT_1537_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_1537_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1537_pause_28',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1537_set_7000_to_tapped_button_29',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1537_jmp_if_7000_any_bits_set_30',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1537_action_queue_sync_32']
    },
    {
        "identifier": 'EVENT_1537_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_1537_pause_28']
    },
    {
        "identifier": 'EVENT_1537_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1537_action_queue_sync_32_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1537_action_queue_sync_32_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_1537_action_queue_sync_32_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_1537_clear_bit_33',
        "command": 'clear_bit',
        "args": [0x7095, 0]
    },
    {
        "identifier": 'EVENT_1537_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7096, 6]
    },
    {
        "identifier": 'EVENT_1537_move_script_to_main_thread_35',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1537_ret_36',
        "command": 'ret'
    }
]
