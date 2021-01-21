from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_709_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_709_face_southwest_1',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_709_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_709_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_709_transfer_to_xyzf_4',
        "command": 'transfer_to_xyzf',
        "args": [2, 48, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_709_object_memory_clear_bit_5',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_709_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_709_set_random_7',
        "command": 'set_random',
        "args": [0x700c, 30]
    },
    {
        "identifier": 'ACTION_709_add_short_8',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_709_load_mem_9',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_709_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_709_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_709_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._049_BIG_SHELL_HIT, 4]
    },
    {
        "identifier": 'ACTION_709_shift_southwest_pixels_13',
        "command": 'shift_southwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_709_db_14',
        "command": 'db',
        "args": [0x3a, 0x18, 0x00, 0x03, 0xf6, 0x82]
    },
    {
        "identifier": 'ACTION_709_jump_to_height_15',
        "command": 'jump_to_height',
        "args": [24]
    },
    {
        "identifier": 'ACTION_709_walk_1_step_southeast_16',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_709_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_709_db_14']
    },
    {
        "identifier": 'ACTION_709_set_bit_18',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_709_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_708_jump_to_height_20']
    }
]
