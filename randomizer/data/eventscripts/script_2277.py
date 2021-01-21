from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2277_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_2277_pause_1',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2277_enter_area_2',
        "command": 'enter_area',
        "args": [Rooms._015_VISTA_HILL, RadialDirections.NORTHWEST, 4, 16, 0, []]
    },
    {
        "identifier": 'EVENT_2277_fade_out_music_to_volume_3',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_4_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [0, 2, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_sequence_playback_off_5',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_5_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_1],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_6_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.LAYER_2],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_async_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_7_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_shift_northwest_pixels_4',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_8_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_9_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_10_SUBSCRIPT_sequence_looping_on_10',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_11_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_12_SUBSCRIPT_sequence_looping_on_8',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [4, 26, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_shift_south_pixels_7',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_sequence_looping_on_9',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_13_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_fade_in_from_black_async_duration_14',
        "command": 'fade_in_from_black_async_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2277_play_music_default_volume_15',
        "command": 'play_music_default_volume',
        "args": [Music._66_BOWSERS_CASTLE_2ND_TIME]
    },
    {
        "identifier": 'EVENT_2277_pause_16',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_2277_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_async_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_17_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_17_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_17_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_17_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_pause_18',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_19_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_19_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_20_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_20_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_21_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_21_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_21_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_21_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_21_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_22_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_22_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_23_SUBSCRIPT_sequence_looping_off_8',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_pause_24',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2277_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [127, 15, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_shift_west_pixels_5',
                "command": 'shift_west_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0x20, 0x01]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_embedded_animation_routine_9',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_shift_south_steps_11',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_shift_south_pixels_12',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_db_13',
                "command": 'db',
                "args": [0x20, 0x00]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_25_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_26_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_26_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 1007]
    },
    {
        "identifier": 'EVENT_2277_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 1008]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_29_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_29_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_29_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_29_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_29_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_sync_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_30_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2277_action_queue_sync_30_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2277_action_queue_async_31_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2277_action_queue_async_31_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2277_pause_32',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_2277_fade_out_to_black_async_duration_33',
        "command": 'fade_out_to_black_async_duration',
        "args": [50]
    },
    {
        "identifier": 'EVENT_2277_pause_34',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_2277_jmp_to_event_35',
        "command": 'jmp_to_event',
        "args": [3868]
    }
]
