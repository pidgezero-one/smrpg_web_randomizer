from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_710_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_710_face_southwest_1',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_710_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_710_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_710_transfer_to_xyzf_4',
        "command": 'transfer_to_xyzf',
        "args": [3, 46, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_710_object_memory_clear_bit_5',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_710_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_710_set_random_7',
        "command": 'set_random',
        "args": [0x700c, 30]
    },
    {
        "identifier": 'ACTION_710_inc_short_8',
        "command": 'inc_short',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_710_load_mem_9',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_710_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_710_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_710_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_710_shift_southwest_pixels_14']
    },
    {
        "identifier": 'ACTION_710_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_710_shift_southwest_pixels_14',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_710_db_15',
        "command": 'db',
        "args": [0x3a, 0x19, 0x00, 0x03, 0x2a, 0x83]
    },
    {
        "identifier": 'ACTION_710_jump_to_height_16',
        "command": 'jump_to_height',
        "args": [24]
    },
    {
        "identifier": 'ACTION_710_walk_1_step_southeast_17',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_710_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_710_db_15']
    },
    {
        "identifier": 'ACTION_710_set_bit_19',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_710_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_708_jump_to_height_20']
    }
]
