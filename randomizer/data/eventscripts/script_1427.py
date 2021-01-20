from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1427_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1427_action_queue_async_0_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1427_action_queue_async_0_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1427_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 4, 'EVENT_1427_remove_from_current_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1427_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 5, 'EVENT_1427_remove_from_current_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1427_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 6, 'EVENT_1427_remove_from_current_level_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1427_jmp_to_event_4',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1427_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1427_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1427_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    },
]
