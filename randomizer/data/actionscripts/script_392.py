from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_392_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_392_shift_north_pixels_1',
        "command": 'shift_north_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_392_shift_south_pixels_2',
        "command": 'shift_south_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_392_shift_north_pixels_3',
        "command": 'shift_north_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_392_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_392_ret_6']
    },
    {
        "identifier": 'ACTION_392_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_392_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_392_ret_6',
        "command": 'ret'
    }
]
