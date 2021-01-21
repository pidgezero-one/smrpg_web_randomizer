from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_363_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_363_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_363_shift_southeast_pixels_2',
        "command": 'shift_southeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_363_jmp_if_mario_in_air_3',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_363_clear_bit_5']
    },
    {
        "identifier": 'ACTION_363_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_363_shift_southeast_pixels_2']
    },
    {
        "identifier": 'ACTION_363_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'ACTION_363_reset_properties_6',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_363_face_northwest_7',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_363_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_363_shift_z_down_pixels_9',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_363_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_363_ret_11',
        "command": 'ret'
    }
]
