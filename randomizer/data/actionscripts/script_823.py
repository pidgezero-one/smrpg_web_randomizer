from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_823_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_823_set_700C_to_object_coord_1',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_823_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x700c, 2176]
    },
    {
        "identifier": 'ACTION_823_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_823_pause_0']
    },
    {
        "identifier": 'ACTION_823_set_700C_to_object_coord_4',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_823_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x700c, 9216]
    },
    {
        "identifier": 'ACTION_823_jmp_if_comparison_result_is_lesser_6',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_823_object_memory_modify_bits_13']
    },
    {
        "identifier": 'ACTION_823_set_700C_to_object_coord_7',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_823_mem_compare_8',
        "command": 'mem_compare',
        "args": [0x700c, 13056]
    },
    {
        "identifier": 'ACTION_823_jmp_if_comparison_result_is_greater_or_equal_9',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_823_object_memory_modify_bits_13']
    },
    {
        "identifier": 'ACTION_823_set_priority_10',
        "command": 'set_priority',
        "args": [0]
    },
    {
        "identifier": 'ACTION_823_shadow_off_11',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_823_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_823_pause_0']
    },
    {
        "identifier": 'ACTION_823_object_memory_modify_bits_13',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_823_shadow_on_14',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_823_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_823_pause_0']
    }
]
