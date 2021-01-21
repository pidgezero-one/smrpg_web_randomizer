from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_396_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_396_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_396_shift_southeast_pixels_2',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_396_shift_northwest_pixels_3',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_396_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_396_ret_6']
    },
    {
        "identifier": 'ACTION_396_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_396_fixed_f_coord_on_0']
    },
    {
        "identifier": 'ACTION_396_ret_6',
        "command": 'ret'
    }
]
