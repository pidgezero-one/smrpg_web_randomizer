from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1828_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1828_set_7000_to_object_coord_1',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1828_jmp_if_7000_equals_short_2',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_1828_db_10']
    },
    {
        "identifier": 'EVENT_1828_jmp_if_mario_in_air_3',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1828_pause_0']
    },
    {
        "identifier": 'EVENT_1828_set_7000_short_mem_to_7000_4',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x703c]
    },
    {
        "identifier": 'EVENT_1828_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1828_set_7000_short_mem_to_7000_6',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7038]
    },
    {
        "identifier": 'EVENT_1828_set_7000_to_object_coord_7',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1828_set_7000_short_mem_to_7000_8',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x703a]
    },
    {
        "identifier": 'EVENT_1828_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1828_pause_0']
    },
    {
        "identifier": 'EVENT_1828_db_10',
        "command": 'db',
        "args": [0xfd, 0x44]
    },
    {
        "identifier": 'EVENT_1828_db_11',
        "command": 'db',
        "args": [0xfd, 0x47]
    },
    {
        "identifier": 'EVENT_1828_run_event_at_return_12',
        "command": 'run_event_at_return',
        "args": [1830]
    },
    {
        "identifier": 'EVENT_1828_ret_13',
        "command": 'ret'
    }
]
