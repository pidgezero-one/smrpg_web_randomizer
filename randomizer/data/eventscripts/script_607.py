from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_607_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 409, 'EVENT_607_store_item_amount_7000_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_run_dialog_2',
        "command": 'run_dialog',
        "args": [2811, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_store_item_amount_7000_4',
        "command": 'store_item_amount_7000',
        "args": [items.CastleKey2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_607_play_sound_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_run_dialog_6',
        "command": 'run_dialog',
        "args": [2811, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_pause_9',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_pause_11',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_apply_solidity_mod_12',
        "command": 'apply_solidity_mod',
        "args": [Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, 1, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_remove_from_current_level_13',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_remove_one_from_inventory_17',
        "command": 'remove_one_from_inventory',
        "args": [items.CastleKey2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_607_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
