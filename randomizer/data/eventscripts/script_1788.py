from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1788_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1788_action_queue_sync_0_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1788_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1788_action_queue_sync_1_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1788_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1788_action_queue_sync_2_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1788_action_queue_sync_2_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1788_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1788_action_queue_sync_3_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1788_action_queue_sync_3_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1788_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
