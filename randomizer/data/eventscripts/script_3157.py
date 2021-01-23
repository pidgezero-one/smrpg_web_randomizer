from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3157_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3157_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [12, 'EVENT_3157_set_7000_to_object_coord_4']
    },
    {
        "identifier": 'EVENT_3157_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3157_action_queue_async_2_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3157_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3157_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_3157_set_7000_to_object_coord_0']
    },
    {
        "identifier": 'EVENT_3157_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3157_jmp_if_7000_not_equals_short_5',
        "command": 'jmp_if_7000_not_equals_short',
        "args": [61, 'EVENT_3157_action_queue_async_2']
    },
    {
        "identifier": 'EVENT_3157_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3157_action_queue_async_6_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3157_action_queue_async_6_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3157_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_3157_set_7000_to_object_coord_0']
    }
]
