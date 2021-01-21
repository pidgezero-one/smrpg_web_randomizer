from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_630_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_630_set_object_memory_bits_1',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_630_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_630_shift_south_pixels_3',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_630_fixed_f_coord_off_4',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_630_face_northwest_5',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_630_fixed_f_coord_on_6',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_630_shift_south_pixels_7',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_630_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_630_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_630_fixed_f_coord_off_10',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_630_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_630_shift_southeast_steps_12',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_630_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_630_face_northwest_14',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_630_fixed_f_coord_on_15',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_630_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_630_set_bit_17',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_630_object_memory_clear_bit_18',
        "command": 'object_memory_clear_bit',
        "args": [0x08, [3, 4]]
    },
    {
        "identifier": 'ACTION_630_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_630_set_solidity_bits_20',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_630_shift_northwest_pixels_21',
        "command": 'shift_northwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_630_shift_southeast_pixels_22',
        "command": 'shift_southeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_630_pause_23',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_630_shift_northwest_pixels_24',
        "command": 'shift_northwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_630_shift_southeast_pixels_25',
        "command": 'shift_southeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_630_pause_26',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_630_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_630_shift_northwest_pixels_21']
    }
]
