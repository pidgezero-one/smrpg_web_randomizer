from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_442_pause_0',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'ACTION_442_face_mario_1',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_442_db_2',
        "command": 'db',
        "args": [0x3a, 0x00, 0x00, 0x05, 0xda, 0x54]
    },
    {
        "identifier": 'ACTION_442_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_442_pause_0']
    },
    {
        "identifier": 'ACTION_442_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_442_sequence_playback_on_5',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_442_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_442_shift_f_direction_steps_7',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_442_face_mario_8',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_442_shift_f_direction_steps_9',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_442_face_mario_10',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_442_shift_f_direction_steps_11',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_442_sequence_playback_off_12',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_442_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_442_pause_0']
    }
]
