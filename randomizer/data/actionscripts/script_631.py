from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_631_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_631_set_object_memory_bits_1',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [1]]
    },
    {
        "identifier": 'ACTION_631_pause_2',
        "command": 'pause',
        "args": [46]
    },
    {
        "identifier": 'ACTION_631_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_631_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_631_face_northwest_5',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_631_fixed_f_coord_on_6',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_631_shift_southeast_steps_7',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_631_shift_southeast_pixels_8',
        "command": 'shift_southeast_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_631_fixed_f_coord_off_9',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_631_face_southeast_10',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_631_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_631_set_solidity_bits_12',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_631_ret_13',
        "command": 'ret'
    }
]
