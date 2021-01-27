from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_983_pause_0',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_983_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_983_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_983_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_983_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_983_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_983_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_983_pause_7',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_983_reset_properties_8',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_983_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_983_shift_northeast_steps_10',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_983_pause_11',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_983_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_983_shift_southwest_steps_3']
    }
]
