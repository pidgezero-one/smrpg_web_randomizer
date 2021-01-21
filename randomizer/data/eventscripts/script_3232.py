from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3232_jmp_to_subroutine_0',
        "command": 'jmp_to_subroutine',
        "args": [0x3171]
    },
    {
        "identifier": 'EVENT_3232_add_short_1',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_3232_jmp_if_var_not_equals_short_2',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 5, 'EVENT_3232_jmp_4']
    },
    {
        "identifier": 'EVENT_3232_set_short_3',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3232_jmp_4',
        "command": 'jmp',
        "args": ['EVENT_3237_clear_bit_9']
    }
]
