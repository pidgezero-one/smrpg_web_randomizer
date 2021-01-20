from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_670_set_bit_7_offset_0',
        "command": 'set_bit_7_offset',
        "args": [0x0158],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_1_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_3_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_670_action_queue_sync_3_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_4_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_670_action_queue_sync_4_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_8_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_9_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_10_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_11_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_670_action_queue_sync_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_670_remember_last_object_14',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7042, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7042, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7042, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7042, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7042, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7042, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7042, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_set_23',
        "command": 'set',
        "args": [0x70ac, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_set_24',
        "command": 'set',
        "args": [0x70b8, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_26',
        "command": 'clear_bit',
        "args": [0x704c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x704c, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x704c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x709f, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x709f, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_fade_out_music_to_volume_31',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_fade_in_from_black_async_32',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_670_ret_33',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
