from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2343_set_7000_to_object_coord_0',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2343_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2343_clear_bit_4']
    },
    {
        "identifier": 'EVENT_2343_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2343_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_2343_set_7000_to_object_coord_0']
    },
    {
        "identifier": 'EVENT_2343_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2343_ret_5',
        "command": 'ret'
    }
]
