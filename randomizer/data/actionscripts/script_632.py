from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_632_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_632_shift_z_up_steps_1',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_632_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_632_shift_z_up_pixels_3',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_632_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_632_shift_z_up_pixels_5',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_632_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_632_shift_z_up_pixels_7',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_632_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_632_shift_z_up_pixels_9',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_632_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_632_shift_z_up_pixels_11',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_632_set_priority_12',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_632_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_632_ret_14',
        "command": 'ret'
    }
]
