from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1386_freeze_camera_0',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1386_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1386_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_sync_1_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [0, 2, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1386_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1386_action_queue_async_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_2_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_2_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_2_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_2_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1386_fade_in_from_black_sync_duration_3',
        "command": 'fade_in_from_black_sync_duration',
        "args": [130]
    },
    {
        "identifier": 'EVENT_1386_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_1386_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_sync_4_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1386_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_1386_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_sync_5_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1386_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1386_action_queue_async_6_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_6_SUBSCRIPT_shift_east_steps_2',
                "command": 'shift_east_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1386_pause_7',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1386_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1386_action_queue_async_8_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1386_fade_out_to_black_async_duration_9',
        "command": 'fade_out_to_black_async_duration',
        "args": [70]
    },
    {
        "identifier": 'EVENT_1386_open_location_10',
        "command": 'open_location',
        "args": [Locations._003_VISTA_HILL, [6, 7]]
    },
    {
        "identifier": 'EVENT_1386_ret_11',
        "command": 'ret'
    }
]
