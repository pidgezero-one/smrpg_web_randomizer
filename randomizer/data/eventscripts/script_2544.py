from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2544_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_2544_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2544_set_7000_to_object_coord_2',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2544_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2544_jmp_if_bit_clear_5']
    },
    {
        "identifier": 'EVENT_2544_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2544_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 5, 'EVENT_2544_apply_tile_mod_10']
    },
    {
        "identifier": 'EVENT_2544_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2544_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2544_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_7, 15]
    },
    {
        "identifier": 'EVENT_2544_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2544_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_2544_action_queue_sync_11']
    },
    {
        "identifier": 'EVENT_2544_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2544_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_jmp_if_bit_clear_1',
                "command": 'jmp_if_bit_clear',
                "args": [0x7043, 0, 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_shift_z_up_steps_4']
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_face_south_3',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_11_SUBSCRIPT_clear_bit_6',
                "command": 'clear_bit',
                "args": [0x7043, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2544_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2544_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_12_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2544_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2544_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_13_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_13_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2544_action_queue_sync_13_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2544_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2544_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_14_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_14_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_14_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_14_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_14_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2544_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2544_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2544_action_queue_async_16_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_jmp_if_bit_clear_4',
                "command": 'jmp_if_bit_clear',
                "args": [0x7099, 7, 'EVENT_2544_run_event_as_subroutine_17']
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_jmp_if_bit_set_5',
                "command": 'jmp_if_bit_set',
                "args": [0x708c, 5, 'EVENT_2544_run_event_as_subroutine_17']
            },
            {
                "identifier": 'EVENT_2544_action_queue_async_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_2544_run_event_as_subroutine_17',
        "command": 'run_event_as_subroutine',
        "args": [3588]
    },
    {
        "identifier": 'EVENT_2544_jmp_if_bit_clear_18',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2544_unfreeze_camera_22']
    },
    {
        "identifier": 'EVENT_2544_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 5, 'EVENT_2544_unfreeze_camera_22']
    },
    {
        "identifier": 'EVENT_2544_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2544_play_sound_21',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6]
    },
    {
        "identifier": 'EVENT_2544_unfreeze_camera_22',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2544_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7099, 7]
    },
    {
        "identifier": 'EVENT_2544_ret_24',
        "command": 'ret'
    }
]
