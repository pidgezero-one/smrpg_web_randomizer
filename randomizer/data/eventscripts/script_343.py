from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_343_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_343_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_343_set_short_3']
    },
    {
        "identifier": 'EVENT_343_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_343_pause_0']
    },
    {
        "identifier": 'EVENT_343_set_short_3',
        "command": 'set_short',
        "args": [0x7010, 0x000a]
    },
    {
        "identifier": 'EVENT_343_set_short_4',
        "command": 'set_short',
        "args": [0x7012, 0x0012]
    },
    {
        "identifier": 'EVENT_343_db_5',
        "command": 'db',
        "args": [0xfd, 0xc9]
    },
    {
        "identifier": 'EVENT_343_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000]
    },
    {
        "identifier": 'EVENT_343_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 354, 'EVENT_343_ret_11']
    },
    {
        "identifier": 'EVENT_343_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_343_apply_tile_mod_9',
        "command": 'apply_tile_mod',
        "args": [Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_343_apply_solidity_mod_10',
        "command": 'apply_solidity_mod',
        "args": [Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_343_ret_11',
        "command": 'ret'
    }
]
