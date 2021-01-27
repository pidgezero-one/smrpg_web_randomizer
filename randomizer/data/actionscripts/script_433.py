from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_433_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_433_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_433_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_433_inc_palette_row_by_3',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_433_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_433_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_433_inc_palette_row_by_6',
        "command": 'inc_palette_row_by',
        "args": [255]
    },
    {
        "identifier": 'ACTION_433_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_433_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_433_set_700C_to_pressed_button_9',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_433_mem_compare_address_10',
        "command": 'mem_compare_address',
        "args": [0x7034]
    },
    {
        "identifier": 'ACTION_433_jmp_if_loaded_memory_is_not_0_11',
        "command": 'jmp_if_loaded_memory_is_not_0',
        "args": ['ACTION_433_pause_8']
    },
    {
        "identifier": 'ACTION_433_inc_palette_row_by_12',
        "command": 'inc_palette_row_by',
        "args": [1]
    },
    {
        "identifier": 'ACTION_433_set_bit_13',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_433_ret_14',
        "command": 'ret'
    }
]
