from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3145_jmp_if_var_equals_byte_0',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70a8, 20, 'EVENT_3145_jmp_to_event_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 2, 'EVENT_3145_set_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_jmp_to_event_2',
        "command": 'jmp_to_event',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_set_4',
        "command": 'set',
        "args": [0x70a7, 166],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_run_event_as_subroutine_5',
        "command": 'run_event_as_subroutine',
        "args": [33],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_set_6',
        "command": 'set',
        "args": [0x7000, 1586],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_set_7',
        "command": 'set',
        "args": [0x70a7, 166],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_set_bit_9',
        "command": 'set_bit',
        "args": [0x7055, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3145_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
