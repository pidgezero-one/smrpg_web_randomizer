from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_242_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_242_shift_z_down_pixels_1',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_242_shift_z_up_pixels_2',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_242_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_988_ret_14']
    },
    {
        "identifier": 'ACTION_242_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_242_set_animation_speed_0']
    }
]
