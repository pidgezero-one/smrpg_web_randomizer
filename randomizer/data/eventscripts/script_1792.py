from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1792_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1792_action_queue_sync_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x09, [7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1792_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1792_action_queue_sync_1_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x09, [7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1792_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1792_action_queue_async_2_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x09, [7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1792_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7050, 5, 'EVENT_1792_jmp_to_event_7']
    },
    {
        "identifier": 'EVENT_1792_set_bit_4',
        "command": 'set_bit',
        "args": [0x7050, 5]
    },
    {
        "identifier": 'EVENT_1792_set_short_5',
        "command": 'set_short',
        "args": [0x701c, 0x0050]
    },
    {
        "identifier": 'EVENT_1792_run_background_event_with_pause_return_on_exit_6',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1790, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_1792_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [15]
    }
]
