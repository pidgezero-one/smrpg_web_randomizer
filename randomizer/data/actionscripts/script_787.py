from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_787_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_787_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [346, 'ACTION_787_set_animation_speed_10']
    },
    {
        "identifier": 'ACTION_787_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_787_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_787_floating_off_4',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_787_set_priority_5',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_787_fixed_f_coord_on_6',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_787_shift_northwest_steps_7',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_787_fixed_f_coord_off_8',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_787_face_northwest_9',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_787_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_787_sequence_playback_off_11',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_787_fixed_f_coord_on_12',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_787_shift_northwest_pixels_13',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_787_shift_southeast_pixels_14',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_787_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_787_shift_northwest_pixels_13']
    }
]
