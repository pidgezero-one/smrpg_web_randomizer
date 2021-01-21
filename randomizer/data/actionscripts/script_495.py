from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_495_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_495_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_495_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_495_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_495_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_495_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_495_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_495_shirt_to_xy_coords_7',
        "command": 'shirt_to_xy_coords',
        "args": [19, 85]
    },
    {
        "identifier": 'ACTION_495_pause_8',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'ACTION_495_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_495_ret_10',
        "command": 'ret'
    }
]
