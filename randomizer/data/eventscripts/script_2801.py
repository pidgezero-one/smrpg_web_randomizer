from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2801_set_bit_0',
        "command": 'set_bit',
        "args": [0x7068, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2801_set_bit_1',
        "command": 'set_bit',
        "args": [0x7070, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2801_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 4, 'EVENT_2801_open_location_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2801_open_location_3',
        "command": 'open_location',
        "args": [Locations._039_BEAN_VALLEY, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2801_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2801_open_location_5',
        "command": 'open_location',
        "args": [Locations._045_BEAN_VALLEY, [6, 7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2801_ret_6',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
