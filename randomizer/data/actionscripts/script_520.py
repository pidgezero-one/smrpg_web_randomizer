from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_520_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_520_shift_northwest_pixels_1',
        "command": 'shift_northwest_pixels',
        "args": [14]
    },
    {
        "identifier": 'ACTION_520_visibility_off_2',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_520_ret_3',
        "command": 'ret'
    }
]
