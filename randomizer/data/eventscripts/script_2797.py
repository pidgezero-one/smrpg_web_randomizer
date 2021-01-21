from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2797_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2797_ret_13']
    },
    {
        "identifier": 'EVENT_2797_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2797_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._081_STAR, 6]
    },
    {
        "identifier": 'EVENT_2797_db_3',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2797_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._145_STAR_HILL_AREA_01, 5, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2797_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2797_db_6',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2797_apply_tile_mod_7',
        "command": 'apply_tile_mod',
        "args": [Rooms._145_STAR_HILL_AREA_01, 7, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2797_pause_8',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2797_db_9',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2797_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._145_STAR_HILL_AREA_01, 2, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2797_apply_solidity_mod_11',
        "command": 'apply_solidity_mod',
        "args": [Rooms._145_STAR_HILL_AREA_01, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_2797_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._126_EMERGE_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2797_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2797_ret_14',
        "command": 'ret'
    }
]
