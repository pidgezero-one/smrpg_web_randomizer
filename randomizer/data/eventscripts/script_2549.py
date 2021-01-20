from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2549_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_run_event_as_subroutine_1',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_6, Rooms._349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, 'EVENT_2549_jmp_if_bit_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 6, 'EVENT_2549_freeze_camera_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._100_BOOSTER_PASS_AREA_01, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_freeze_camera_6',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2549_action_queue_sync_7_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2549_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2549_action_queue_sync_8_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2549_action_queue_sync_9_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2549_action_queue_sync_10_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_12_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2549_action_queue_async_14_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_jmp_if_bit_clear_4',
                "command": 'jmp_if_bit_clear',
                "args": [0x7099, 7, 'EVENT_2549_clear_bit_20']
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x708d, 6, 'EVENT_2549_unfreeze_camera_15']
            },
            {
                "identifier": 'EVENT_2549_action_queue_async_14_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_2549_unfreeze_camera_15',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2549_clear_bit_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x708d, 6, 'EVENT_2549_clear_bit_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_play_sound_19',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2549_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
