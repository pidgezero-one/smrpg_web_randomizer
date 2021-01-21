from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1681_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [65]
    },
    {
        "identifier": 'EVENT_1681_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._424_BELOME_TEMPLE_AREA_03_PIPE_TO_ROOM_DETERMINED_BY_FORTUNE, RadialDirections.SOUTH, 20, 74, 0, []]
    },
    {
        "identifier": 'EVENT_1681_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_1690_fade_in_from_black_sync_2']
    }
]
