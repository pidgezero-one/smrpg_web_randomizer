from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_318_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_318_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_318_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_318_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_318_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_318_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7024, 0x700c]
    },
    {
        "identifier": 'ACTION_318_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x700c, 0x70ae]
    },
    {
        "identifier": 'ACTION_318_mem_compare_7',
        "command": 'mem_compare',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_318_jmp_if_loaded_memory_is_not_0_8',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['ACTION_318_pause_3']
    },
    {
        "identifier": 'ACTION_318_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_318_object_memory_clear_bit_10',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_318_pause_11',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_318_start_loop_n_times_12',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_318_visibility_off_13',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_318_pause_14',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_318_visibility_on_15',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_318_pause_16',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_318_end_loop_17',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_318_visibility_off_18',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_318_object_memory_set_bit_19',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_318_ret_20',
        "command": 'ret'
    }
]
