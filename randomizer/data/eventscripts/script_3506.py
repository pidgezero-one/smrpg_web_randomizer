from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3506_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 1, 'EVENT_3506_disable_trigger_2']
    },
    {
        "identifier": 'EVENT_3506_ret_1',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3506_disable_trigger_2',
        "command": 'disable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3506_stop_background_event_3',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_3506_enable_controls_until_return_4',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3506_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 716]
    },
    {
        "identifier": 'EVENT_3506_set_6',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3506_add_max_FP_7000_7',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_3506_inc_8',
        "command": 'inc',
        "args": [0x70b1]
    },
    {
        "identifier": 'EVENT_3506_pause_9',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3506_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_shift_west_pixels_4',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [4, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_10_SUBSCRIPT_shift_west_pixels_6',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3506_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3506_action_queue_async_11_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_11_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_11_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_11_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3506_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3506_action_queue_sync_12_SUBSCRIPT_shift_east_pixels_0',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_12_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_sync_12_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3506_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3506_action_queue_async_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_13_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_13_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3506_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3506_action_queue_async_16']
    },
    {
        "identifier": 'EVENT_3506_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 717]
    },
    {
        "identifier": 'EVENT_3506_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_shift_southeast_pixels_11',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_dec_short_12',
                "command": 'dec_short',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_end_loop_13',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3506_action_queue_async_16_SUBSCRIPT_set_solidity_bits_15',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3506_jmp_if_bit_clear_17',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_3506_set_bit_19']
    },
    {
        "identifier": 'EVENT_3506_set_temp_action_script_sync_18',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_7, 718]
    },
    {
        "identifier": 'EVENT_3506_set_bit_19',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_3506_enable_controls_until_return_20',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3506_resume_background_event_21',
        "command": 'resume_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_3506_enable_trigger_22',
        "command": 'enable_trigger',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3506_ret_23',
        "command": 'ret'
    }
]
