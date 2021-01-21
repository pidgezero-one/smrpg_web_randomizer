from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2619_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2619_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2619_action_queue_sync_0_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 3]
            },
            {
                "identifier": 'EVENT_2619_action_queue_sync_0_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2619_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2619_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2619_remove_from_current_level_2',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2619_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2619_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2619_action_queue_sync_3_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2619_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2619_star_mask_expand_from_screen_center_4',
        "command": 'star_mask_expand_from_screen_center'
    },
    {
        "identifier": 'EVENT_2619_pause_short_5',
        "command": 'pause_short',
        "args": [384]
    },
    {
        "identifier": 'EVENT_2619_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2619_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2619_action_queue_sync_6_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2619_star_mask_shrink_to_screen_center_7',
        "command": 'star_mask_shrink_to_screen_center'
    },
    {
        "identifier": 'EVENT_2619_pause_script_until_effect_done_8',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_2619_stop_embedded_action_script_9',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_2619_jmp_to_event_10',
        "command": 'jmp_to_event',
        "args": [3799]
    },
    {
        "identifier": 'EVENT_2619_ret_11',
        "command": 'ret'
    }
]
