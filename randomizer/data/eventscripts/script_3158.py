from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3158_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7058, 0, 'EVENT_3158_ret_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_set_bit_1',
        "command": 'set_bit',
        "args": [0x7058, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_set_7010_to_object_xyz_3',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_add_short_4',
        "command": 'add_short',
        "args": [0x7014, 0x0200],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_create_packet_at_7010_coords_jmp_if_null_5',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 'EVENT_3158_set_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_set_6',
        "command": 'set',
        "args": [0x7000, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_add_max_FP_7000_7',
        "command": 'add_max_FP_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3158_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
