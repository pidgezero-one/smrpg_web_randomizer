from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2404_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 3, 'EVENT_2404_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 4, 'EVENT_2404_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_stop_all_background_events_2',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_fade_out_music_3',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_set_bit_4',
        "command": 'set_bit',
        "args": [0x708b, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_shift_west_pixels_4',
                "command": 'shift_west_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0xc0, 0xff]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [54]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_priority_11',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_shift_east_pixels_12',
                "command": 'shift_east_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_priority_13',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2404_pause_6',
        "command": 'pause',
        "args": [64],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_play_music_default_volume_7',
        "command": 'play_music_default_volume',
        "args": [Music._45_HEART_BEATING_A_LITTLE_FASTER_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_stop_embedded_action_script_8',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2404_action_queue_async_9_SUBSCRIPT_shift_northeast_steps_8',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2404_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2404_action_queue_sync_10_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2404_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2404_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2404_action_queue_async_11_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2404_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2403_remove_from_current_level_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2404_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
