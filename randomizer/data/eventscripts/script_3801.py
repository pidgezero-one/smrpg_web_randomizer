from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3801_pause_0',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3801_run_event_sequence_1',
        "command": 'run_event_sequence',
        "args": [EventSequences._13_RUN_STAR_PIECE_END_SEQUENCE, 0x05]
    },
    {
        "identifier": 'EVENT_3801_pause_2',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_3801_jmp_to_event_3',
        "command": 'jmp_to_event',
        "args": [2295]
    }
]
