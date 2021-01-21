from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_556_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127]
    },
    {
        "identifier": 'EVENT_556_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x705d, 1, 'EVENT_556_action_queue_sync_4']
    },
    {
        "identifier": 'EVENT_556_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 4, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_556_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 4, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_8_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_9_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_10_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_remember_last_object_11',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_556_summon_to_level_12',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._087_ROSE_TOWN_ITEM_SHOP]
    },
    {
        "identifier": 'EVENT_556_summon_to_level_13',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._087_ROSE_TOWN_ITEM_SHOP]
    },
    {
        "identifier": 'EVENT_556_summon_to_level_14',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._091_ROSE_TOWN_COUPLES_HOUSE]
    },
    {
        "identifier": 'EVENT_556_jmp_if_object_not_in_level_15',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_10, Rooms._084_ROSE_TOWN_OUTSIDE, 'EVENT_556_run_background_event_23']
    },
    {
        "identifier": 'EVENT_556_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_async_16_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_jmp_if_object_not_in_level_17',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 'EVENT_556_apply_tile_mod_29']
    },
    {
        "identifier": 'EVENT_556_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 4, 'EVENT_556_set_41']
    },
    {
        "identifier": 'EVENT_556_run_background_event_19',
        "command": 'run_background_event',
        "args": [557, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_556_set_bit_20',
        "command": 'set_bit',
        "args": [0x709f, 5]
    },
    {
        "identifier": 'EVENT_556_fade_in_from_black_async_21',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_556_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_556_run_background_event_23',
        "command": 'run_background_event',
        "args": [557, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_556_fade_in_from_black_async_24',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_556_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 4, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_556_pause_26',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_556_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_556_action_queue_sync_27_SUBSCRIPT_shift_north_pixels_9',
                "command": 'shift_north_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_556_pause_28',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_556_apply_tile_mod_29',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_556_apply_solidity_mod_30',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_556_jmp_if_bit_clear_31',
        "command": 'jmp_if_bit_clear',
        "args": [0x709f, 5, 'EVENT_556_set_bit_33']
    },
    {
        "identifier": 'EVENT_556_play_sound_32',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_556_set_bit_33',
        "command": 'set_bit',
        "args": [0x709f, 5]
    },
    {
        "identifier": 'EVENT_556_set_bit_34',
        "command": 'set_bit',
        "args": [0x7060, 4]
    },
    {
        "identifier": 'EVENT_556_jmp_if_object_not_in_level_35',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_10, Rooms._084_ROSE_TOWN_OUTSIDE, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_556_remove_from_level_36',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._084_ROSE_TOWN_OUTSIDE]
    },
    {
        "identifier": 'EVENT_556_remove_from_current_level_37',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_556_run_background_event_38',
        "command": 'run_background_event',
        "args": [557, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_556_fade_in_from_black_async_39',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_556_ret_40',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_556_set_41',
        "command": 'set',
        "args": [0x70a9, 30]
    },
    {
        "identifier": 'EVENT_556_run_background_event_42',
        "command": 'run_background_event',
        "args": [557, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_556_set_bit_43',
        "command": 'set_bit',
        "args": [0x7061, 4]
    },
    {
        "identifier": 'EVENT_556_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_529_pause_action_script_27']
    }
]
