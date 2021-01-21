from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_44_pause_0',
        "command": 'pause',
        "args": [55]
    },
    {
        "identifier": 'ACTION_44_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_44_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_44_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_44_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_44_shift_northeast_pixels_5',
        "command": 'shift_northeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_44_pause_6',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_44_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_44_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_44_jump_to_height_silent_9',
        "command": 'jump_to_height_silent',
        "args": [40]
    },
    {
        "identifier": 'ACTION_44_shift_southwest_pixels_10',
        "command": 'shift_southwest_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_44_pause_11',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'ACTION_44_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_44_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_44_shift_northeast_pixels_14',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_44_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_44_shift_northeast_pixels_5']
    }
]
