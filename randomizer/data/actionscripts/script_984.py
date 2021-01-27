from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_984_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_984_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_984_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_984_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_984_face_southwest_5']
    },
    {
        "identifier": 'ACTION_984_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_984_pause_2']
    },
    {
        "identifier": 'ACTION_984_face_southwest_5',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_984_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_984_face_southeast_7',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_984_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_984_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_984_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_984_pause_11',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_984_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_984_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_984_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_984_pause_2']
    }
]
