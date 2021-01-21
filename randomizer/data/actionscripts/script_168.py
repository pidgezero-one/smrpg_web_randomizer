from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_168_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_168_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_168_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_168_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_168_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_168_shift_northwest_pixels_5',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_168_pause_6',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_168_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_168_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_168_jump_to_height_silent_9',
        "command": 'jump_to_height_silent',
        "args": [36]
    },
    {
        "identifier": 'ACTION_168_shift_southeast_pixels_10',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_168_pause_11',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'ACTION_168_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_168_sequence_looping_on_2']
    }
]
