from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_882_set_solidity_bits_0',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_882_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_882_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_882_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_882_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'ACTION_882_face_mario_5',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_882_shift_f_direction_steps_6',
        "command": 'shift_f_direction_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_882_jmp_if_random_above_128_7',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_882_set_animation_speed_9']
    },
    {
        "identifier": 'ACTION_882_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_882_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_882_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_882_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_882_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_882_set_animation_speed_2']
    }
]
