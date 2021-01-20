from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3706_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_set_7000_to_current_level_1',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 114, 'EVENT_3706_jmp_if_object_not_in_level_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_object_not_in_level_3',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_5, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_start_battle_4',
        "command": 'start_battle',
        "args": [0x0063, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3705_jmp_to_event_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3706_set_temp_action_script_sync_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_level_10',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_object_not_in_level_15',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_start_battle_16',
        "command": 'start_battle',
        "args": [0x0063, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_3705_jmp_to_event_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3706_set_temp_action_script_sync_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_current_level_19',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_current_level_21',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_level_22',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_level_23',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_remove_from_level_24',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_fade_in_from_black_async_25',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_set_temp_action_script_sync_27',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 889],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_set_7000_to_current_level_28',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_jmp_if_var_equals_short_29',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 410, 'EVENT_3706_set_temp_action_script_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_set_temp_action_script_sync_30',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_4, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_fade_in_from_black_async_31',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_set_temp_action_script_sync_33',
        "command": 'set_temp_action_script_sync',
        "args": [AreaObjects.NPC_5, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_fade_in_from_black_async_34',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3706_ret_35',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
