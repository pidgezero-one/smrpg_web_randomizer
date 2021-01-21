from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_998_face_southeast_0',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_998_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_998_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_998_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_998_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_998_clear_solidity_bits_6']
    },
    {
        "identifier": 'ACTION_998_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_998_pause_3']
    },
    {
        "identifier": 'ACTION_998_clear_solidity_bits_6',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_998_sequence_looping_on_7',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_998_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_998_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_998_jump_to_height_silent_10',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_998_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_998_sequence_looping_off_12',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_998_pause_13',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_998_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_997_sequence_playback_on_0']
    }
]
