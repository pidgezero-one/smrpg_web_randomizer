from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_324_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_324_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_324_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_324_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_324_walk_1_step_southeast_16']
    },
    {
        "identifier": 'ACTION_324_shift_northeast_steps_4',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_324_set_solidity_bits_5',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_324_floating_on_6',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_324_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_324_visibility_off_8',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_324_pause_9',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'ACTION_324_face_southwest_10',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_324_visibility_on_11',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_324_shift_southwest_steps_12',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_324_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_324_transfer_to_xyzf_14',
        "command": 'transfer_to_xyzf',
        "args": [6, 88, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_324_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_324_walk_1_step_southeast_16',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_324_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_324_transfer_to_xyzf_14']
    }
]
