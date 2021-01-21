from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_1009_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_1009_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_1009_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_1009_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [14]
    },
    {
        "identifier": 'ACTION_1009_jump_to_height_4',
        "command": 'jump_to_height',
        "args": [80]
    },
    {
        "identifier": 'ACTION_1009_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_1009_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_1009_shadow_off_7',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_1009_shift_south_steps_8',
        "command": 'shift_south_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_1009_visibility_off_9',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_1009_ret_10',
        "command": 'ret'
    }
]
