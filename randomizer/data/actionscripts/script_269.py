from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_269_set_movement_bits_0',
        "command": 'set_movement_bits',
        "args": [[_0x0AFlags.BIT_0, _0x0AFlags.CANT_WALK_UNDER]]
    },
    {
        "identifier": 'ACTION_269_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_269_pause_2',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_269_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_269_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_269_set_700C_to_object_coord_5',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_269_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_269_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_269_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_269_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_269_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_269_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_269_shift_z_down_steps_13']
    },
    {
        "identifier": 'ACTION_269_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_269_shift_z_down_steps_13',
        "command": 'shift_z_down_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_269_set_700C_to_7000_short_mem_14',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7032]
    },
    {
        "identifier": 'ACTION_269_face_east_7C_15',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_16',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_269_set_sprite_sequence_22']
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_17',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_269_set_sprite_sequence_22']
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_18',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_269_set_sprite_sequence_22']
    },
    {
        "identifier": 'ACTION_269_jmp_if_700C_equals_short_19',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_269_set_sprite_sequence_22']
    },
    {
        "identifier": 'ACTION_269_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_269_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_269_clear_solidity_bits_23']
    },
    {
        "identifier": 'ACTION_269_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_269_clear_solidity_bits_23',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_269_set_animation_speed_24',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_269_set_solidity_bits_25',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_269_start_loop_n_times_26',
        "command": 'start_loop_n_times',
        "args": [39]
    },
    {
        "identifier": 'ACTION_269_shift_z_up_pixels_27',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_269_shift_f_direction_pixels_28',
        "command": 'shift_f_direction_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_269_end_loop_29',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_269_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_269_set_animation_speed_4']
    }
]
