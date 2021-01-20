from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_435_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 0, 'EVENT_435_action_queue_sync_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_435_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 10, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_435_action_queue_sync_1_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_435_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_435_jmp_if_object_not_in_level_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_435_action_queue_sync_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 22, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_435_action_queue_sync_3_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_435_jmp_if_object_not_in_level_4',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_1, Rooms._123_PIPE_VAULT_AREA_01, 'EVENT_435_jmp_if_object_not_in_level_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_435_action_queue_sync_5_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_435_jmp_if_object_not_in_level_6',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_2, Rooms._123_PIPE_VAULT_AREA_01, 'EVENT_435_jmp_if_object_not_in_level_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_435_action_queue_sync_7_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_435_jmp_if_object_not_in_level_8',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_3, Rooms._123_PIPE_VAULT_AREA_01, 'EVENT_435_jmp_if_object_not_in_level_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_435_action_queue_sync_9_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_435_jmp_if_object_not_in_level_10',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._123_PIPE_VAULT_AREA_01, 'EVENT_435_run_background_event_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_435_action_queue_sync_11_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_435_run_background_event_12',
        "command": 'run_background_event',
        "args": [3329, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 0, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_435_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
