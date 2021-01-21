from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_494_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_494_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_494_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_494_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_494_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_494_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_494_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_494_shift_northwest_pixels_7',
        "command": 'shift_northwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_494_pause_8',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_494_face_northeast_9',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_494_pause_10',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_494_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_494_shift_southeast_pixels_12',
        "command": 'shift_southeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_494_visibility_off_13',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_494_pause_14',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_494_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_494_ret_16',
        "command": 'ret'
    }
]
