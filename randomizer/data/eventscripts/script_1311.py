from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1311_set_0',
        "command": 'set',
        "args": [0x70a7, 140],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1311_apply_tile_mod_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_run_dialog_3',
        "command": 'run_dialog',
        "args": [2801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_apply_solidity_mod_6',
        "command": 'apply_solidity_mod',
        "args": [Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_remove_one_from_inventory_9',
        "command": 'remove_one_from_inventory',
        "args": [items.RoomKey],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1311_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
