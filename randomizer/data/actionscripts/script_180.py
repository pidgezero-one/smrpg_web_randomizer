from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_180_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_180_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_180_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_180_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_180_pause_4',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_face_southwest_5',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_180_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_face_northeast_7',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_180_pause_8',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_face_southeast_9',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_180_pause_10',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_shift_southwest_steps_11',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_180_shift_northwest_steps_12',
        "command": 'shift_northwest_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_180_walk_1_step_northeast_13',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_180_shift_northwest_steps_14',
        "command": 'shift_northwest_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_180_shift_southwest_steps_15',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_180_pause_16',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_face_northwest_17',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_180_pause_18',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_face_southeast_19',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_180_pause_20',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_180_shift_northeast_steps_21',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_180_shift_southeast_steps_22',
        "command": 'shift_southeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_180_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_180_sequence_looping_on_0']
    }
]
