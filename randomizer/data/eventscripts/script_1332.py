from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1332_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1332_ret_17']
    },
    {
        "identifier": 'EVENT_1332_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 3, 'EVENT_1332_apply_tile_mod_10']
    },
    {
        "identifier": 'EVENT_1332_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1332_pause_3',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1332_apply_tile_mod_4',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1332_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1332_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1332_start_battle_7',
        "command": 'start_battle',
        "args": [0x002e, 12]
    },
    {
        "identifier": 'EVENT_1332_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1332_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_1338_pause_0']
    },
    {
        "identifier": 'EVENT_1332_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 35, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1332_pause_11',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1332_apply_tile_mod_12',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1332_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1332_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1332_add_short_15',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_1332_set_bit_16',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1332_ret_17',
        "command": 'ret'
    }
]
