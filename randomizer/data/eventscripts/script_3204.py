from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3204_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 4, 'EVENT_3204_jmp_to_event_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3204_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 2, 'EVENT_3204_jmp_to_event_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3204_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3204_action_queue_sync_2_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_2_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_2_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3204_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3204_action_queue_sync_3_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_3_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_3_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3204_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3204_action_queue_sync_4_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_4_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_sync_4_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3204_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3204_action_queue_async_5_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_async_5_SUBSCRIPT_face_mario_1',
                "command": 'face_mario',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_async_5_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3204_action_queue_async_5_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3204_jmp_to_event_6',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    }
]
