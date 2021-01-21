from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_1010_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_1010_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_1010_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_1010_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_1010_shift_northwest_pixels_4',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_1010_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_1010_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_1010_ret_7',
        "command": 'ret'
    }
]
