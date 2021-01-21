from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_1014_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_1014_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_1014_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_1014_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_1014_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_1014_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_1014_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_1014_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_1014_shift_southeast_steps_8',
        "command": 'shift_southeast_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_1014_shift_southwest_steps_9',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_1014_shift_northwest_steps_10',
        "command": 'shift_northwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_1014_bounce_to_xy_with_height_11',
        "command": 'bounce_to_xy_with_height',
        "args": [17, 27, 2]
    },
    {
        "identifier": 'ACTION_1014_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_1014_set_animation_speed_0']
    }
]
