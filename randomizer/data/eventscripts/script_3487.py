from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3487_disable_trigger_0',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 719],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_add_frog_coins_2',
        "command": 'add_frog_coins',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_set_7000_to_object_coord_3',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_mem_compare_4',
        "command": 'mem_compare',
        "args": [0x7000, 12288],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_jmp_if_comparison_result_is_greater_or_equal_5',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3487_set_bit_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_mem_compare_6',
        "command": 'mem_compare',
        "args": [0x7000, 8704],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_jmp_if_comparison_result_is_greater_or_equal_7',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3487_set_bit_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_mem_compare_8',
        "command": 'mem_compare',
        "args": [0x7000, 5120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_jmp_if_comparison_result_is_greater_or_equal_9',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3487_set_bit_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_set_bit_10',
        "command": 'set_bit',
        "args": [0x7079, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_set_bit_12',
        "command": 'set_bit',
        "args": [0x7079, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_set_bit_14',
        "command": 'set_bit',
        "args": [0x7079, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_set_bit_16',
        "command": 'set_bit',
        "args": [0x7079, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3487_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
