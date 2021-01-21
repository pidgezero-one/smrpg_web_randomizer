from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_565_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_565_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_565_shift_northeast_steps_2',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_565_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_565_shift_northeast_steps_4',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_565_shift_northeast_pixels_5',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_565_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_565_shift_northwest_pixels_7',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_565_shift_northeast_steps_8',
        "command": 'shift_northeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_565_visibility_off_9',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_565_ret_10',
        "command": 'ret'
    }
]
