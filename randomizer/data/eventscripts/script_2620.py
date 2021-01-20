from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2620_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2620_clear_bit_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_2620_clear_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_2620_clear_bit_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_2620_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_6',
        "command": 'set_short',
        "args": [0x7010, 0x0008],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_7',
        "command": 'set_short',
        "args": [0x7012, 0x0060],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_8',
        "command": 'set_short',
        "args": [0x7014, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_db_9',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_create_packet_at_7010_coords_jmp_if_null_10',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._049_HAMMER_SPARKS_SFX, 'EVENT_2620_jmp_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_2620_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_13',
        "command": 'set_short',
        "args": [0x7010, 0x000a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_14',
        "command": 'set_short',
        "args": [0x7012, 0x0065],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_15',
        "command": 'set_short',
        "args": [0x7014, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_db_16',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_create_packet_at_7010_coords_jmp_if_null_17',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._049_HAMMER_SPARKS_SFX, 'EVENT_2620_jmp_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_2620_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_20',
        "command": 'set_short',
        "args": [0x7010, 0x000d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_21',
        "command": 'set_short',
        "args": [0x7012, 0x006b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_set_short_22',
        "command": 'set_short',
        "args": [0x7014, 0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_db_23',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_create_packet_at_7010_coords_jmp_if_null_24',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._049_HAMMER_SPARKS_SFX, 'EVENT_2620_jmp_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2620_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_2620_pause_0'],
        "subscript": []
    },
]
