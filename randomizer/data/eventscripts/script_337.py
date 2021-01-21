from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_337_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_337_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_337_set_2',
        "command": 'set',
        "args": [0x70a9, 0]
    },
    {
        "identifier": 'EVENT_337_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [9]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_face_south_10',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_3_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_337_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_337_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_337_action_queue_sync_5_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_337_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_337_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_337_action_queue_sync_5_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_337_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_337_action_queue_async_6_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_6_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_6_SUBSCRIPT_add_z_coord_1_step_2',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_6_SUBSCRIPT_dec_z_coord_1_step_3',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_337_run_dialog_7',
        "command": 'run_dialog',
        "args": [608, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_337_remember_last_object_8',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_337_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_337_action_queue_async_9_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_337_action_queue_async_9_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_337_action_queue_async_9_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_337_run_event_as_subroutine_10',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_337_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_337_action_queue_async_11_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_337_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_337_unsync_action_script_13',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_337_ret_14',
        "command": 'ret'
    }
]
