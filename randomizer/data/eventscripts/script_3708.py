from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3708_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_set_1',
        "command": 'set',
        "args": [0x70a7, 132],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_store_7000_item_quantity_to_70A7_2',
        "command": 'store_7000_item_quantity_to_70A7',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_3708_play_sound_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_unfreeze_all_npcs_4',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_ret_5',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_pause_7',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_apply_solidity_mod_9',
        "command": 'apply_solidity_mod',
        "args": [Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_apply_solidity_mod_10',
        "command": 'apply_solidity_mod',
        "args": [Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_remove_from_current_level_12',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_11],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_11, Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_remove_one_from_inventory_15',
        "command": 'remove_one_from_inventory',
        "args": [items.CastleKey1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_unfreeze_all_npcs_16',
        "command": 'unfreeze_all_npcs',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3708_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
