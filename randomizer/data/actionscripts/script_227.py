from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_227_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_pause_2',
        "command": 'pause',
        "args": [98]
    },
    {
        "identifier": 'ACTION_227_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_pause_4',
        "command": 'pause',
        "args": [162]
    },
    {
        "identifier": 'ACTION_227_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_pause_6',
        "command": 'pause',
        "args": [162]
    },
    {
        "identifier": 'ACTION_227_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_pause_8',
        "command": 'pause',
        "args": [214]
    },
    {
        "identifier": 'ACTION_227_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_pause_10',
        "command": 'pause',
        "args": [216]
    },
    {
        "identifier": 'ACTION_227_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_227_pause_12',
        "command": 'pause',
        "args": [384]
    },
    {
        "identifier": 'ACTION_227_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_227_add_z_coord_1_step_14',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_227_ret_15',
        "command": 'ret'
    }
]
