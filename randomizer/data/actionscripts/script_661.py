from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_661_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_661_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_661_db_2',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x02, 0xe7, 0x78]
    },
    {
        "identifier": 'ACTION_661_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_661_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_661_set_animation_speed_1']
    },
    {
        "identifier": 'ACTION_661_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_661_jump_to_height_silent_6',
        "command": 'jump_to_height_silent',
        "args": [64]
    },
    {
        "identifier": 'ACTION_661_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_661_db_8',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xec, 0x78]
    },
    {
        "identifier": 'ACTION_661_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_661_set_animation_speed_1']
    }
]
