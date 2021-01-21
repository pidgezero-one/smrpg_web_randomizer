from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_254_pause_0',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_254_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'EVENT_254_ret_5']
    },
    {
        "identifier": 'EVENT_254_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x707c, 2, 'EVENT_254_ret_5']
    },
    {
        "identifier": 'EVENT_254_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x707c, 3]
    },
    {
        "identifier": 'EVENT_254_create_packet_at_object_coords_jmp_if_null_4',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._022_SPARKLES_MOVE_N, AreaObjects.MARIO, 'EVENT_254_pause_0']
    },
    {
        "identifier": 'EVENT_254_ret_5',
        "command": 'ret'
    }
]
