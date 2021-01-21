from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1340_set_0',
        "command": 'set',
        "args": [0x70a7, 141]
    },
    {
        "identifier": 'EVENT_1340_store_7000_item_quantity_to_70A7_1',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_1340_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1340_apply_tile_mod_5']
    },
    {
        "identifier": 'EVENT_1340_run_dialog_3',
        "command": 'run_dialog',
        "args": [2801, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1340_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1340_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1340_apply_solidity_mod_6',
        "command": 'apply_solidity_mod',
        "args": [Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1340_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_14]
    },
    {
        "identifier": 'EVENT_1340_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_14, Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    },
    {
        "identifier": 'EVENT_1340_remove_one_from_inventory_9',
        "command": 'remove_one_from_inventory',
        "args": [items.ElderKey]
    },
    {
        "identifier": 'EVENT_1340_ret_10',
        "command": 'ret'
    }
]
