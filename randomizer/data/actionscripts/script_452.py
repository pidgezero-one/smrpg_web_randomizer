from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_452_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_452_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7045, 7, 'ACTION_452_pause_3']
    },
    {
        "identifier": 'ACTION_452_pause_2',
        "command": 'pause',
        "args": [176]
    },
    {
        "identifier": 'ACTION_452_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_452_db_4',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x02, 0xc9, 0x57]
    },
    {
        "identifier": 'ACTION_452_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_452_pause_3']
    },
    {
        "identifier": 'ACTION_452_sequence_looping_on_6',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_452_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_452_pause_8',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_452_shift_northwest_steps_9',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_452_pause_10',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_452_face_northeast_11',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_452_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_452_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_452_pause_14',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_452_face_southwest_15',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_452_pause_16',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_452_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_452_shift_northwest_steps_9']
    }
]
