from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1564_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1564_set_7016_to_object_xyz_1',
        "command": 'set_7016_to_object_xyz',
        "args": [0x90]
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_2_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_2_SUBSCRIPT_run_away_shift_1',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_2_SUBSCRIPT_face_south_2',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_2_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_2_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1564_action_queue_sync_3_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_5_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._009_GREEN_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_5_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_5_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_5_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_set_7000_to_object_coord_6',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.F, []]
    },
    {
        "identifier": 'EVENT_1564_jmp_if_7000_equals_short_7',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_1564_set_action_script_sync_10']
    },
    {
        "identifier": 'EVENT_1564_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 782]
    },
    {
        "identifier": 'EVENT_1564_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1564_pause_11']
    },
    {
        "identifier": 'EVENT_1564_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 783]
    },
    {
        "identifier": 'EVENT_1564_pause_11',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1564_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1564_set_7000_to_tapped_button_13',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1564_jmp_if_7000_all_bits_clear_14',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_1564_pause_12']
    },
    {
        "identifier": 'EVENT_1564_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1564_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000]
    },
    {
        "identifier": 'EVENT_1564_mem_7000_shift_left_17',
        "command": 'mem_7000_shift_left',
        "args": [0x7000, 8]
    },
    {
        "identifier": 'EVENT_1564_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7000]
    },
    {
        "identifier": 'EVENT_1564_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1564_mem_7000_and_const_20',
        "command": 'mem_7000_and_const',
        "args": [0x00ff]
    },
    {
        "identifier": 'EVENT_1564_jmp_if_7000_equals_short_21',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_1564_action_queue_async_29']
    },
    {
        "identifier": 'EVENT_1564_jmp_if_7000_equals_short_22',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_1564_action_queue_async_32']
    },
    {
        "identifier": 'EVENT_1564_jmp_if_7000_equals_short_23',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_1564_action_queue_async_35']
    },
    {
        "identifier": 'EVENT_1564_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1564_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_face_east_7C_0',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [192]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_set_short_3',
                "command": 'set_short',
                "args": [0x7034, 0xeeee]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_4',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._032_BLUE_CLOUD, AreaObjects.MARIO, 'EVENT_1564_action_queue_async_26_SUBSCRIPT_set_animation_speed_5']
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_26_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_move_script_to_background_thread_2_27',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1564_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_1564_action_queue_sync_44']
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_29_SUBSCRIPT_face_east_7C_0',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_29_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_29_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_29_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [192]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_set_short_30',
        "command": 'set_short',
        "args": [0x7030, 0x0001]
    },
    {
        "identifier": 'EVENT_1564_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_1564_clear_bit_37']
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_32_SUBSCRIPT_face_east_7C_0',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_32_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_32_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_32_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [192]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_set_short_33',
        "command": 'set_short',
        "args": [0x7030, 0x0002]
    },
    {
        "identifier": 'EVENT_1564_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_1564_clear_bit_37']
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_35_SUBSCRIPT_face_east_7C_0',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_35_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_35_SUBSCRIPT_floating_off_2',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_35_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [192]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_set_short_36',
        "command": 'set_short',
        "args": [0x7030, 0x0004]
    },
    {
        "identifier": 'EVENT_1564_clear_bit_37',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1564_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1564_set_short_39',
        "command": 'set_short',
        "args": [0x7034, 0xeeee]
    },
    {
        "identifier": 'EVENT_1564_create_packet_at_object_coords_jmp_if_null_40',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, AreaObjects.MARIO, 'EVENT_1564_pause_41']
    },
    {
        "identifier": 'EVENT_1564_pause_41',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1564_move_script_to_background_thread_2_42',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1564_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7030]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_walk_f_direction_16_pixels_3',
                "command": 'walk_f_direction_16_pixels'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1564_action_queue_async_43_SUBSCRIPT_set_short_mem_2']
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_1564_action_queue_async_43_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1564_action_queue_sync_44_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1564_clear_bit_45',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1564_move_script_to_main_thread_46',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1564_ret_47',
        "command": 'ret'
    }
]
