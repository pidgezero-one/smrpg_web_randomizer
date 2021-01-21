from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_335_pause_0',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_335_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_335_transfer_to_xyzf_2',
        "command": 'transfer_to_xyzf',
        "args": [15, 87, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_335_transfer_xyzf_pixels_3',
        "command": 'transfer_xyzf_pixels',
        "args": [240, 0, 20, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_335_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_335_turn_random_direction_5',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_335_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_335_floating_on_7',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_335_jump_to_height_silent_8',
        "command": 'jump_to_height_silent',
        "args": [128]
    },
    {
        "identifier": 'ACTION_335_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_335_shift_f_direction_steps_10',
        "command": 'shift_f_direction_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_335_ret_11',
        "command": 'ret'
    }
]
