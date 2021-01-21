from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_629_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_629_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 120, 'ACTION_629_pause_13']
    },
    {
        "identifier": 'ACTION_629_set_object_memory_bits_2',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_629_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_629_face_southeast_4',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_629_fixed_f_coord_on_5',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_629_shift_z_down_pixels_6',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_629_shift_east_pixels_7',
        "command": 'shift_east_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_629_fixed_f_coord_off_8',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_629_face_southwest_9',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_629_fixed_f_coord_on_10',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_629_shift_east_pixels_11',
        "command": 'shift_east_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_629_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_629_pause_13',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_629_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_629_pause_15',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_629_set_sprite_sequence_16',
        "command": 'set_sprite_sequence',
        "args": [21, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_629_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_629_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_629_jmp_if_random_above_128_19',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_629_pause_13']
    },
    {
        "identifier": 'ACTION_629_pause_20',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_629_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_629_pause_13']
    }
]
