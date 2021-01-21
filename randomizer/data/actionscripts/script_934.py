from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_934_sequence_playback_off_0',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_934_sequence_looping_off_1',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_934_pause_2',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_934_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_934_pause_2']
    },
    {
        "identifier": 'ACTION_934_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_934_floating_off_5',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_934_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_934_shift_z_up_pixels_7',
        "command": 'shift_z_up_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_934_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_934_shift_z_up_pixels_9',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_934_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_934_shift_z_up_pixels_11',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_934_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_934_shift_z_up_pixels_13',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_934_pause_14',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_934_floating_on_15',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_934_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_934_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_934_sequence_playback_off_0']
    }
]
