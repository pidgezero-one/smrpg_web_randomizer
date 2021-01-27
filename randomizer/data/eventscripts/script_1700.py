from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1700_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1700_ret_26']
    },
    {
        "identifier": 'EVENT_1700_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_1700_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1700_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1700_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_1700_pause_action_script_9']
    },
    {
        "identifier": 'EVENT_1700_set_bit_5',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1700_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1700_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1700_run_background_event_8',
        "command": 'run_background_event',
        "args": [1705, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1700_pause_action_script_9',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1700_set_7000_to_object_coord_10',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1700_mem_compare_val_11',
        "command": 'mem_compare_val',
        "args": [12]
    },
    {
        "identifier": 'EVENT_1700_jmp_if_comparison_result_is_greater_or_equal_12',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1700_mem_compare_val_14']
    },
    {
        "identifier": 'EVENT_1700_ret_13',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1700_mem_compare_val_14',
        "command": 'mem_compare_val',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1700_jmp_if_comparison_result_is_lesser_15',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1700_set_7000_to_7000_short_mem_17']
    },
    {
        "identifier": 'EVENT_1700_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1700_set_7000_to_7000_short_mem_17',
        "command": 'set_7000_to_7000_short_mem',
        "args": [0x703e]
    },
    {
        "identifier": 'EVENT_1700_mem_compare_val_18',
        "command": 'mem_compare_val',
        "args": [26]
    },
    {
        "identifier": 'EVENT_1700_jmp_if_loaded_memory_is_not_0_19',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['EVENT_1700_set_21']
    },
    {
        "identifier": 'EVENT_1700_add_short_20',
        "command": 'add_short',
        "args": [0x7024, 0x0080]
    },
    {
        "identifier": 'EVENT_1700_set_21',
        "command": 'set',
        "args": [0x70a9, 26]
    },
    {
        "identifier": 'EVENT_1700_set_short_22',
        "command": 'set_short',
        "args": [0x703e, 0x001a]
    },
    {
        "identifier": 'EVENT_1700_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 478]
    },
    {
        "identifier": 'EVENT_1700_pause_24',
        "command": 'pause',
        "args": [34]
    },
    {
        "identifier": 'EVENT_1700_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 477]
    },
    {
        "identifier": 'EVENT_1700_ret_26',
        "command": 'ret'
    }
]
