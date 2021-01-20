from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1586_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7079, 0, 'EVENT_1586_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x7000, 30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1586_set_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_set_5',
        "command": 'set',
        "args": [0x7000, 161],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_1586_set_short_mem_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_add_7',
        "command": 'add',
        "args": [0x7000, 65522],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x702c, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_pause_9',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_1586_pause_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_dec_short_11',
        "command": 'dec_short',
        "args": [0x702c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_jmp_if_var_not_equals_short_12',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702c, 0, 'EVENT_1586_pause_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 597],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_11, 167],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1586_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
