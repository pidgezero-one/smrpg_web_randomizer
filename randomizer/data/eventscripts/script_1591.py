from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1591_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 6, 'EVENT_1591_ret_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1591_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1591_action_queue_sync_1_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_1_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_1_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_1_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_1_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_1_SUBSCRIPT_floating_on_5',
                "command": 'floating_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1591_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1591_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_2_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_2_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1591_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0x5b]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._109_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_jump_to_height_11',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_shift_east_pixels_12',
                "command": 'shift_east_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_end_loop_13',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_start_loop_n_times_14',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_db_16',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0x6d]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._109_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_jump_to_height_18',
                "command": 'jump_to_height',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_shift_east_pixels_19',
                "command": 'shift_east_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1591_action_queue_sync_3_SUBSCRIPT_end_loop_20',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1591_set_bit_4',
        "command": 'set_bit',
        "args": [0x704e, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1591_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
