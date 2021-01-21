from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1353_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 2, 'EVENT_1353_pause_3']
    },
    {
        "identifier": 'EVENT_1353_run_dialog_1',
        "command": 'run_dialog',
        "args": [2801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1353_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1353_pause_3',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1353_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_1353_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1353_apply_solidity_mod_6',
        "command": 'apply_solidity_mod',
        "args": [Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1353_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_1353_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS]
    },
    {
        "identifier": 'EVENT_1353_pause_9',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1353_remove_one_from_inventory_10',
        "command": 'remove_one_from_inventory',
        "args": [items.RoomKey]
    },
    {
        "identifier": 'EVENT_1353_ret_11',
        "command": 'ret'
    }
]
