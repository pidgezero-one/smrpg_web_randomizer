from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_391_start_loop_n_times_0',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_391_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_391_shift_north_pixels_2',
        "command": 'shift_north_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_391_shift_south_pixels_3',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_391_shift_north_pixels_4',
        "command": 'shift_north_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_391_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_391_ret_6',
        "command": 'ret'
    }
]
