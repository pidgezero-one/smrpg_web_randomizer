from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_383_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_383_reset_properties_1',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_383_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_383_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_383_floating_off_4',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_383_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_383_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_383_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_383_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_113_jmp_if_bit_set_0']
    }
]
