from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_663_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_663_walk_1_step_southwest_1',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_663_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_663_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_663_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_663_transfer_to_xyzf_5',
        "command": 'transfer_to_xyzf',
        "args": [16, 85, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_663_set_bit_6',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'ACTION_663_ret_7',
        "command": 'ret'
    }
]
