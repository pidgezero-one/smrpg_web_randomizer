from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_928_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'ACTION_928_visibility_off_17']
    },
    {
        "identifier": 'ACTION_928_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_928_jump_to_subroutine_2',
        "command": 'jump_to_subroutine',
        "args": [0xabb7]
    },
    {
        "identifier": 'ACTION_928_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_928_jump_to_subroutine_4',
        "command": 'jump_to_subroutine',
        "args": [0xabb7]
    },
    {
        "identifier": 'ACTION_928_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_928_jump_to_subroutine_6',
        "command": 'jump_to_subroutine',
        "args": [0xabb7]
    },
    {
        "identifier": 'ACTION_928_shift_southeast_steps_7',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_928_jump_to_subroutine_8',
        "command": 'jump_to_subroutine',
        "args": [0xabb7]
    },
    {
        "identifier": 'ACTION_928_shift_southeast_steps_9',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_928_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_928_jmp_if_bit_set_0']
    },
    {
        "identifier": 'ACTION_928_face_northeast_11',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_928_jump_to_height_silent_12',
        "command": 'jump_to_height_silent',
        "args": [32]
    },
    {
        "identifier": 'ACTION_928_pause_13',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_928_jump_to_height_silent_14',
        "command": 'jump_to_height_silent',
        "args": [32]
    },
    {
        "identifier": 'ACTION_928_pause_15',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_928_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_928_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_928_clear_solidity_bits_18',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_928_object_memory_set_bit_19',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_928_ret_20',
        "command": 'ret'
    }
]
