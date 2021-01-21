from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3849_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3849_db_1',
        "command": 'db',
        "args": [0xfd, 0x44]
    },
    {
        "identifier": 'EVENT_3849_db_2',
        "command": 'db',
        "args": [0xfd, 0x45]
    },
    {
        "identifier": 'EVENT_3849_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70de, 18, 'EVENT_3849_set_short_7']
    },
    {
        "identifier": 'EVENT_3849_set_short_4',
        "command": 'set_short',
        "args": [0x7036, 0x0000]
    },
    {
        "identifier": 'EVENT_3849_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._079_ROSE_WAY_MAIN_AREA, RadialDirections.NORTHEAST, 4, 56, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3849_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3849_set_short_7',
        "command": 'set_short',
        "args": [0x7036, 0x118d]
    },
    {
        "identifier": 'EVENT_3849_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED, RadialDirections.SOUTHWEST, 26, 77, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3849_ret_9',
        "command": 'ret'
    }
]
