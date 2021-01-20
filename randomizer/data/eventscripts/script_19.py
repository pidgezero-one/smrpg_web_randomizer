from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_19_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_19_set_bit_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_19_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [255],
        "subscript": []
    },
    {
        "identifier": 'EVENT_19_set_bit_2',
        "command": 'set_bit',
        "args": [0x707c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_19_jmp_to_subroutine_3',
        "command": 'jmp_to_subroutine',
        "args": [0x0c69],
        "subscript": []
    },
    {
        "identifier": 'EVENT_19_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x707c, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_19_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
