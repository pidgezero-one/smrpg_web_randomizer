from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2055_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_2055_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN, RadialDirections.SOUTH, 29, 46, 0, [_0x68Flags.SHOW_MESSAGE]]
    },
    {
        "identifier": 'EVENT_2055_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_2055_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [1584]
    }
]
