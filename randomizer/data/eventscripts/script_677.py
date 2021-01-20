from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_677_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_async_0_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_pause_1',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_async_2_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 5, 'EVENT_677_summon_to_current_level_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 3, 'EVENT_677_fade_in_from_black_async_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_summon_to_current_level_8',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_summon_to_current_level_10',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_summon_to_current_level_11',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_12_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_13_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [18, 88, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_677_action_queue_sync_14_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_15_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 76, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_677_action_queue_sync_15_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [2, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_16_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [22, 73, 2, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_17_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [2, 252, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_677_remember_last_object_18',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_12, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_677_action_queue_sync_23_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [0, 120, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_677_action_queue_sync_23_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_677_fade_in_from_black_async_24',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_677_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
