from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_549_dec_0',
        "command": 'dec',
        "args": [0x70bb]
    },
    {
        "identifier": 'ACTION_549_reset_properties_1',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_549_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_549_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_549_pause_4',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_549_set_solidity_bits_5',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_549_jmp_if_random_above_66_6',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_549_face_mario_10']
    },
    {
        "identifier": 'ACTION_549_turn_random_direction_7',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_549_walk_1_step_f_direction_8',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_549_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_549_set_solidity_bits_5']
    },
    {
        "identifier": 'ACTION_549_face_mario_10',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_549_walk_1_step_f_direction_11',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_549_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_549_set_solidity_bits_5']
    }
]
