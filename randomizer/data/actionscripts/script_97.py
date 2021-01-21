from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_97_pause_0',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_97_transfer_to_xyzf_1',
        "command": 'transfer_to_xyzf',
        "args": [8, 106, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_97_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_97_fixed_f_coord_off_3',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_97_set_solidity_bits_4',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_97_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_97_clear_solidity_bits_6',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_0]]
    },
    {
        "identifier": 'ACTION_97_floating_on_7',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_97_shift_northeast_steps_8',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_97_shift_northwest_steps_9',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_97_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_97_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_97_face_northeast_12',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_97_set_solidity_bits_13',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_97_ret_14',
        "command": 'ret'
    }
]
