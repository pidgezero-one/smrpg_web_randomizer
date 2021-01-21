from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1694_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 0, 'EVENT_1694_set_7016_to_object_xyz_3']
    },
    {
        "identifier": 'EVENT_1694_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_1694_set_7016_to_object_xyz_3']
    },
    {
        "identifier": 'EVENT_1694_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1694_set_7016_to_object_xyz_3',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1694_add_short_4',
        "command": 'add_short',
        "args": [0x7016, 0x0030]
    },
    {
        "identifier": 'EVENT_1694_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_run_away_transfer_2',
                "command": 'run_away_transfer'
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_face_south_6',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_1694_action_queue_sync_5_SUBSCRIPT_set_priority_7',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_jmp_to_subroutine_6',
        "command": 'jmp_to_subroutine',
        "args": [0x3292]
    },
    {
        "identifier": 'EVENT_1694_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x704f, 0, 'EVENT_1694_action_queue_async_13']
    },
    {
        "identifier": 'EVENT_1694_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_8_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_8_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_8_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_8_SUBSCRIPT_shift_south_steps_4',
                "command": 'shift_south_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_jmp_to_subroutine_9',
        "command": 'jmp_to_subroutine',
        "args": [0x32aa]
    },
    {
        "identifier": 'EVENT_1694_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_10_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_set_bit_11',
        "command": 'set_bit',
        "args": [0x704f, 0]
    },
    {
        "identifier": 'EVENT_1694_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1694_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_13_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_13_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_13_SUBSCRIPT_shift_north_steps_4',
                "command": 'shift_north_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_jmp_to_subroutine_14',
        "command": 'jmp_to_subroutine',
        "args": [0x32aa]
    },
    {
        "identifier": 'EVENT_1694_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_15_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x704f, 0]
    },
    {
        "identifier": 'EVENT_1694_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1694_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_1694_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_sync_19_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_20_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_20_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_20_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_20_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_pause_21',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1694_play_sound_22',
        "command": 'play_sound',
        "args": [Sounds._048_MINECART_START, 6]
    },
    {
        "identifier": 'EVENT_1694_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1694_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1694_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_sync_25_SUBSCRIPT_object_memory_modify_bits_0',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_pause_26',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1694_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._113_OPEN_CHAMBER_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1694_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1694_action_queue_async_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_28_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_28_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_28_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1694_action_queue_async_28_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1694_ret_29',
        "command": 'ret'
    }
]
