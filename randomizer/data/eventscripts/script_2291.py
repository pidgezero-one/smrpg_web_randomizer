from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2291_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._249_GAME_INTRO_VISTA_HILL, RadialDirections.NORTHEAST, 4, 18, 0, []]
    },
    {
        "identifier": 'EVENT_2291_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2291_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2291_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2291_action_queue_sync_2_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [0, 2, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2291_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2291_action_queue_async_3_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_3_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_3_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_3_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2291_read_from_address_4',
        "command": 'read_from_address',
        "args": [0x91d2]
    },
    {
        "identifier": 'EVENT_2291_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._249_GAME_INTRO_VISTA_HILL, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2291_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2291_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_2291_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2291_action_queue_sync_7_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2291_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_2291_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2291_action_queue_sync_8_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2291_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2291_action_queue_async_9_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2291_action_queue_async_9_SUBSCRIPT_shift_east_steps_2',
                "command": 'shift_east_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2291_pause_10',
        "command": 'pause',
        "args": [75]
    },
    {
        "identifier": 'EVENT_2291_fade_out_to_black_async_duration_11',
        "command": 'fade_out_to_black_async_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2291_jmp_to_event_12',
        "command": 'jmp_to_event',
        "args": [147]
    }
]
