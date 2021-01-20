from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_14_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_14_clear_bit_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [81],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7064, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7064, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7064, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7064, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_set_6',
        "command": 'set',
        "args": [0x70da, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_set_7',
        "command": 'set',
        "args": [0x70db, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_set_8',
        "command": 'set',
        "args": [0x70dc, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_set_9',
        "command": 'set',
        "args": [0x70dd, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_fade_in_from_black_sync_10',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_14_ret_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'EVENT_14_ret_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x707c, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_create_packet_at_object_coords_jmp_if_null_14',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_14_ret_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_14_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
