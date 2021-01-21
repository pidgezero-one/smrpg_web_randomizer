from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_258_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_258_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_258_turn_random_direction_2',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_258_jump_to_height_silent_3',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_258_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_258_db_5',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xc5, 0x2f]
    },
    {
        "identifier": 'ACTION_258_walk_1_step_northeast_6',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_258_turn_random_direction_7',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_258_jump_to_height_silent_8',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_258_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_258_db_10',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0xd1, 0x2f]
    },
    {
        "identifier": 'ACTION_258_walk_1_step_southwest_11',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_258_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_258_set_animation_speed_0']
    }
]
