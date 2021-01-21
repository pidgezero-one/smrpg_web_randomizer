from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_620_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x3c, [6]]
    },
    {
        "identifier": 'ACTION_620_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_620_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_620_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'ACTION_620_shift_z_up_pixels_4',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_620_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'ACTION_620_visibility_off_17']
    },
    {
        "identifier": 'ACTION_620_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_620_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_620_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [31]
    },
    {
        "identifier": 'ACTION_620_shift_z_up_pixels_9',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_620_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'ACTION_620_visibility_off_17']
    },
    {
        "identifier": 'ACTION_620_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_620_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_620_start_loop_n_times_13',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'ACTION_620_shift_z_up_pixels_14',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_620_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7076, 0, 'ACTION_620_visibility_off_17']
    },
    {
        "identifier": 'ACTION_620_end_loop_16',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_620_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_620_ret_18',
        "command": 'ret'
    }
]
