from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_181_visibility_on_0',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_181_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_181_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_181_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_181_pause_4',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_181_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_181_pause_6',
        "command": 'pause',
        "args": [72]
    },
    {
        "identifier": 'ACTION_181_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'ACTION_181_ret_8',
        "command": 'ret'
    }
]
