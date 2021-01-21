from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_337_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_337_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_337_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 172, 'ACTION_337_set_palette_row_20']
    },
    {
        "identifier": 'ACTION_337_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 177, 'ACTION_337_set_palette_row_20']
    },
    {
        "identifier": 'ACTION_337_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 163, 'ACTION_337_set_palette_row_24']
    },
    {
        "identifier": 'ACTION_337_inc_palette_row_by_5',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_337_db_6',
        "command": 'db',
        "args": [0xfd, 0x9c, 0x05]
    },
    {
        "identifier": 'ACTION_337_db_7',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_337_db_8',
        "command": 'db',
        "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_337_pause_9',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_337_db_10',
        "command": 'db',
        "args": [0x25, 0x40, 0x00, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_337_pause_11',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_337_bpl_26_27_28_12',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_337_set_700C_to_current_level_13',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_337_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 172, 'ACTION_337_set_palette_row_22']
    },
    {
        "identifier": 'ACTION_337_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 177, 'ACTION_337_set_palette_row_22']
    },
    {
        "identifier": 'ACTION_337_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 163, 'ACTION_337_set_palette_row_26']
    },
    {
        "identifier": 'ACTION_337_inc_palette_row_by_17',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_337_object_memory_clear_bit_18',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_337_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_337_set_palette_row_20',
        "command": 'set_palette_row',
        "args": [2]
    },
    {
        "identifier": 'ACTION_337_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_337_db_6']
    },
    {
        "identifier": 'ACTION_337_set_palette_row_22',
        "command": 'set_palette_row',
        "args": [1]
    },
    {
        "identifier": 'ACTION_337_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_337_object_memory_clear_bit_18']
    },
    {
        "identifier": 'ACTION_337_set_palette_row_24',
        "command": 'set_palette_row',
        "args": [3]
    },
    {
        "identifier": 'ACTION_337_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_337_db_6']
    },
    {
        "identifier": 'ACTION_337_set_palette_row_26',
        "command": 'set_palette_row',
        "args": [2]
    },
    {
        "identifier": 'ACTION_337_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_337_object_memory_clear_bit_18']
    }
]
