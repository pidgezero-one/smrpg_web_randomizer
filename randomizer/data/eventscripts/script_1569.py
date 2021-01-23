from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1569_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 0, 'EVENT_1569_set_short_5']
    },
    {
        "identifier": 'EVENT_1569_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1569_mem_compare_val_2',
        "command": 'mem_compare_val',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1569_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1569_set_short_5']
    },
    {
        "identifier": 'EVENT_1569_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1569_set_short_5',
        "command": 'set_short',
        "args": [0x702c, 0x00a0]
    },
    {
        "identifier": 'EVENT_1569_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1569_dec_short_7',
        "command": 'dec_short',
        "args": [0x702c]
    },
    {
        "identifier": 'EVENT_1569_jmp_if_var_not_equals_short_8',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 0, 'EVENT_1569_pause_6']
    },
    {
        "identifier": 'EVENT_1569_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1569_set_short_13']
    },
    {
        "identifier": 'EVENT_1569_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 597]
    },
    {
        "identifier": 'EVENT_1569_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 167]
    },
    {
        "identifier": 'EVENT_1569_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 1, 'EVENT_1569_ret_20']
    },
    {
        "identifier": 'EVENT_1569_set_short_13',
        "command": 'set_short',
        "args": [0x702c, 0x0050]
    },
    {
        "identifier": 'EVENT_1569_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1569_dec_short_15',
        "command": 'dec_short',
        "args": [0x702c]
    },
    {
        "identifier": 'EVENT_1569_jmp_if_var_not_equals_short_16',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 0, 'EVENT_1569_pause_14']
    },
    {
        "identifier": 'EVENT_1569_jmp_if_bit_set_17',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1569_ret_20']
    },
    {
        "identifier": 'EVENT_1569_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 597]
    },
    {
        "identifier": 'EVENT_1569_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 167]
    },
    {
        "identifier": 'EVENT_1569_ret_20',
        "command": 'ret'
    }
]
