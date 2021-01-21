from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2521_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_2521_ret_12']
    },
    {
        "identifier": 'EVENT_2521_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_2521_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._081_STAR, 6]
    },
    {
        "identifier": 'EVENT_2521_store_01_to_0248_3',
        "command": 'store_01_to_0248'
    },
    {
        "identifier": 'EVENT_2521_db_4',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2521_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._157_STAR_HILL_AREA_03, 11, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2521_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2521_db_7',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2521_apply_tile_mod_8',
        "command": 'apply_tile_mod',
        "args": [Rooms._157_STAR_HILL_AREA_03, 12, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2521_add_9',
        "command": 'add',
        "args": [0x70ae, 0x01]
    },
    {
        "identifier": 'EVENT_2521_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 6, 'EVENT_2522_pause_0']
    },
    {
        "identifier": 'EVENT_2521_store_00_to_0248_11',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_2521_ret_12',
        "command": 'ret'
    }
]
