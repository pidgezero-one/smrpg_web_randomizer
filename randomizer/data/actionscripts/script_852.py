from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_852_visibility_on_0',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_852_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_852_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_852_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_852_reset_properties_4',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_852_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_852_pause_6',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_852_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_852_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_852_shift_northwest_pixels_9',
        "command": 'shift_northwest_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_852_shift_southwest_steps_10',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_852_walk_1_step_southeast_11',
        "command": 'walk_1_step_southeast'
    },
    {
        "identifier": 'ACTION_852_shift_northeast_steps_12',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_852_walk_1_step_northwest_13',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_852_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_852_shift_southwest_steps_10']
    }
]
