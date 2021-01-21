from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_182_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_182_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_182_sequence_playback_off_2',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_182_shift_z_up_pixels_3',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_182_pause_4',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_182_shift_z_down_pixels_5',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_182_pause_6',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_182_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_182_pause_9']
    },
    {
        "identifier": 'ACTION_182_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_182_shift_z_up_pixels_3']
    },
    {
        "identifier": 'ACTION_182_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_182_jmp_if_bit_clear_10',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'ACTION_182_pause_9']
    },
    {
        "identifier": 'ACTION_182_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_182_clear_solidity_bits_0']
    },
    {
        "identifier": 'ACTION_182_ret_12',
        "command": 'ret'
    }
]
