from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2364_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_0_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_0_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_0_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_1_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_1_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_2_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_2_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_4_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_4_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_4_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_5_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_5_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2364_action_queue_sync_6_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_jmp_if_bit_clear_7',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_2364_fade_in_from_black_async_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_enable_controls_until_return_8',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_freeze_camera_9',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_async_10_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_10_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_10_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_10_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_10_SUBSCRIPT_sequence_playback_off_4',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_10_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2364_action_queue_async_12_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_shadow_on_4',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2364_action_queue_async_12_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2364_action_queue_async_12_SUBSCRIPT_pause_6']
            }
        ]
    },
    {
        "identifier": 'EVENT_2364_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_unfreeze_camera_14',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_enable_controls_until_return_15',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2364_run_event_as_subroutine_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_fade_in_from_black_async_18',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_run_event_as_subroutine_19',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2364_clear_bit_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7048, 1, 'EVENT_2364_clear_bit_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 5, 'EVENT_2364_clear_bit_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2364_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
