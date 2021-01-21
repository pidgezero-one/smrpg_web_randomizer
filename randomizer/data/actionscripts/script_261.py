from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_261_db_0',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_261_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_261_walk_1_step_northeast_2',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_261_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_261_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_261_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_261_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_261_pause_7',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_261_walk_1_step_northeast_8',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_261_visibility_off_9',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_261_ret_10',
        "command": 'ret'
    }
]
