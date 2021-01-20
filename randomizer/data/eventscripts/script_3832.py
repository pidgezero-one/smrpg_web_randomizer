from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3832_jmp_if_present_in_current_level_0',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_0, 'EVENT_3832_play_sound_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_set_1',
        "command": 'set',
        "args": [0x70a7, 32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_add_3',
        "command": 'add',
        "args": [0x70c8, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_disable_trigger_in_level_4',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_disable_trigger_in_level_5',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_disable_trigger_in_level_6',
        "command": 'disable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [3837],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_set_7000_to_current_level_10',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 484, 'EVENT_3832_apply_tile_mod_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 492, 'EVENT_3832_apply_tile_mod_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_3832_set_action_script_sync_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3832_set_action_script_sync_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_apply_tile_mod_17',
        "command": 'apply_tile_mod',
        "args": [Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3832_ret_19',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
