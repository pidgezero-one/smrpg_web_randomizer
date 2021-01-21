from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_561_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 0, 'EVENT_561_action_queue_async_2']
    },
    {
        "identifier": 'EVENT_561_jmp_to_subroutine_1',
        "command": 'jmp_to_subroutine',
        "args": [0x10c3]
    },
    {
        "identifier": 'EVENT_561_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_561_action_queue_async_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_561_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [265]
    }
]
