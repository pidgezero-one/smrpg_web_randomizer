from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_521_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_521_shift_northwest_pixels_1',
        "command": 'shift_northwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_521_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_521_shift_southwest_pixels_3',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_521_pause_4',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_521_shift_southeast_pixels_5',
        "command": 'shift_southeast_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_521_pause_6',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_521_shift_northeast_pixels_7',
        "command": 'shift_northeast_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_521_pause_8',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_521_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_521_set_animation_speed_0']
    }
]
