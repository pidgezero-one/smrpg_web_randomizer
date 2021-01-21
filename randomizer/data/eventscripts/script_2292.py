from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2292_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._441_ENDING_CREDITS_TOADOFSKY_CONDUCTS_CHOIR, RadialDirections.NORTHEAST, 3, 17, 0, []]
    },
    {
        "identifier": 'EVENT_2292_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2292_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2292_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_sync_2_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [0, 2, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2292_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2292_action_queue_async_3_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2292_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2292_action_queue_async_4_SUBSCRIPT_shift_north_pixels_0',
                "command": 'shift_north_pixels',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2292_set_bit_7_offset_5',
        "command": 'set_bit_7_offset',
        "args": [0x0158]
    },
    {
        "identifier": 'EVENT_2292_star_mask_expand_from_screen_center_6',
        "command": 'star_mask_expand_from_screen_center'
    },
    {
        "identifier": 'EVENT_2292_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2292_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 1015]
    },
    {
        "identifier": 'EVENT_2292_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2292_clear_bit_7_offset_10',
        "command": 'clear_bit_7_offset',
        "args": [0x0158]
    },
    {
        "identifier": 'EVENT_2292_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2292_action_queue_sync_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2292_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_sync_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [145]
            },
            {
                "identifier": 'EVENT_2292_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2292_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2292_action_queue_async_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_12_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_12_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_12_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2292_action_queue_async_12_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2292_pause_13',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2292_star_mask_shrink_to_screen_center_14',
        "command": 'star_mask_shrink_to_screen_center'
    },
    {
        "identifier": 'EVENT_2292_pause_15',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2292_jmp_to_event_16',
        "command": 'jmp_to_event',
        "args": [3801]
    },
    {
        "identifier": 'EVENT_2292_ret_17',
        "command": 'ret'
    }
]
