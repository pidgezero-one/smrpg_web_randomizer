from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3713_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 257]
    },
    {
        "identifier": 'EVENT_3713_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 890]
    },
    {
        "identifier": 'EVENT_3713_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3713_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3713_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_4, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3713_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x7000, 12032]
    },
    {
        "identifier": 'EVENT_3713_jmp_if_comparison_result_is_lesser_6',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3713_jmp_if_object_not_in_level_8']
    },
    {
        "identifier": 'EVENT_3713_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_3713_jmp_if_object_not_in_level_2']
    },
    {
        "identifier": 'EVENT_3713_jmp_if_object_not_in_level_8',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3713_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3713_set_bit_10',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3713_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_4, 256]
    },
    {
        "identifier": 'EVENT_3713_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3713_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3713_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_3713_clear_bit_16']
    },
    {
        "identifier": 'EVENT_3713_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_3713_pause_13']
    },
    {
        "identifier": 'EVENT_3713_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3713_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_3713_jmp_to_event_18',
        "command": 'jmp_to_event',
        "args": [3713]
    }
]
