from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_642_stop_sound_0',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_1',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_2',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_3',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_enter_area_4',
        "command": 'enter_area',
        "args": [Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL, RadialDirections.SOUTHWEST, 6, 27, 3, [_0x68Flags.RUN_ENTRANCE_EVENT, _0x68Flags.Z_HALF]]
    },
    {
        "identifier": 'EVENT_642_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_642_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_642_start_embedded_action_script_async_F1_7',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_642_start_embedded_action_script_async_F1_7_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_642_start_embedded_action_script_async_F1_7_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_642_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_642_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_8_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [18, 20]
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_8_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_642_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_642_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_9_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [18, 19]
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_9_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_642_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_642_remember_last_object_10',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_642_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_642_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_642_action_queue_async_12_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_642_action_queue_async_12_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_642_action_queue_async_12_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [21, 42, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_642_pause_13',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_642_set_action_script_async_14',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_642_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_642_action_queue_async_15_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_642_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x704c, 5]
    },
    {
        "identifier": 'EVENT_642_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_642_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_642_stop_sound_19',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_20',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_21',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_22',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_642_ret_27',
        "command": 'ret'
    }
]
