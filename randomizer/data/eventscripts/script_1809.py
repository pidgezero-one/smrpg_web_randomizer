from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1809_set_bit_0',
        "command": 'set_bit',
        "args": [0x7067, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_set_bit_1',
        "command": 'set_bit',
        "args": [0x706f, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x708c, 4, 'EVENT_1809_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_set_3',
        "command": 'set',
        "args": [0x70df, 43],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_open_location_4',
        "command": 'open_location',
        "args": [Locations._043_LANDS_END, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_set_6',
        "command": 'set',
        "args": [0x70df, 37],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_open_location_7',
        "command": 'open_location',
        "args": [Locations._037_LANDS_END, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1809_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
