from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_653_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_653_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_653_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 455, 'ACTION_653_set_700C_to_pressed_button_6']
    },
    {
        "identifier": 'ACTION_653_set_700C_to_pressed_button_3',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_653_mem_compare_4',
        "command": 'mem_compare',
        "args": [0x700c, 30]
    },
    {
        "identifier": 'ACTION_653_jmp_if_comparison_result_is_greater_or_equal_5',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_653_set_vram_priority_11']
    },
    {
        "identifier": 'ACTION_653_set_700C_to_pressed_button_6',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_653_add_7',
        "command": 'add',
        "args": [0x700c, 65534]
    },
    {
        "identifier": 'ACTION_653_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x700c]
    },
    {
        "identifier": 'ACTION_653_db_9',
        "command": 'db',
        "args": [0x97, 0x10]
    },
    {
        "identifier": 'ACTION_653_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_653_set_700C_to_pressed_button_6']
    },
    {
        "identifier": 'ACTION_653_set_vram_priority_11',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_653_set_700C_to_pressed_button_12',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_653_add_13',
        "command": 'add',
        "args": [0x700c, 65534]
    },
    {
        "identifier": 'ACTION_653_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x700c]
    },
    {
        "identifier": 'ACTION_653_transfer_to_object_xy_15',
        "command": 'transfer_to_object_xy',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'ACTION_653_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_653_set_700C_to_pressed_button_12']
    }
]
