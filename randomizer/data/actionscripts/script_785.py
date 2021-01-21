from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_785_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_785_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_785_floating_off_2',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_785_set_priority_3',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_785_fixed_f_coord_on_4',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_785_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_785_fixed_f_coord_off_6',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_785_shift_northeast_steps_7',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_785_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_785_sequence_playback_off_9',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_785_fixed_f_coord_on_10',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_785_shift_northeast_pixels_11',
        "command": 'shift_northeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_785_shift_southwest_pixels_12',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_785_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_785_shift_northeast_pixels_11']
    }
]
