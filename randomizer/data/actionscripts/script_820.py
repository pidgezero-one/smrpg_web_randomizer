from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_820_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._010_TRAMPOLINE, 4]
    },
    {
        "identifier": 'ACTION_820_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 6, 'ACTION_820_set_animation_speed_3']
    },
    {
        "identifier": 'ACTION_820_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_820_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_820_jump_to_height_silent_4',
        "command": 'jump_to_height_silent',
        "args": [136]
    },
    {
        "identifier": 'ACTION_820_shift_f_direction_pixels_5',
        "command": 'shift_f_direction_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_820_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_820_shift_f_direction_pixels_5']
    },
    {
        "identifier": 'ACTION_820_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_820_set_solidity_bits_8',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_820_ret_9',
        "command": 'ret'
    }
]
