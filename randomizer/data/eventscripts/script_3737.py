from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3737_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3585_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_3737_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3737_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [22, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_sync_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3737_action_queue_sync_1_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3737_action_queue_sync_1_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3737_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3737_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_2_SUBSCRIPT_walk_1_step_east_1',
                "command": 'walk_1_step_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_3737_fade_in_from_black_sync_3',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3737_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_sequence_looping_off_9',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [19, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [22, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [9, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_start_loop_n_times_17',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_shift_southwest_pixels_18',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_shift_northeast_pixels_20',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_end_loop_21',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_reset_properties_22',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_face_southwest_23',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_sequence_looping_on_24',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_animation_speed_25',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3737_action_queue_async_4_SUBSCRIPT_floating_on_28',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3737_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3737_fade_out_to_black_async_6',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3737_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._371_NIMBUS_LAND_FALL_FROM_PLATFORM_1ST, RadialDirections.NORTHEAST, 27, 29, 6, []]
    },
    {
        "identifier": 'EVENT_3737_run_event_at_return_8',
        "command": 'run_event_at_return',
        "args": [3745]
    },
    {
        "identifier": 'EVENT_3737_ret_9',
        "command": 'ret'
    }
]
