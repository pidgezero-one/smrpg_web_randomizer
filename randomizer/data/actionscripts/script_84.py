from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_84_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_84_pause_1',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_84_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_84_shift_southwest_pixels_3',
        "command": 'shift_southwest_pixels',
        "args": [25]
    },
    {
        "identifier": 'ACTION_84_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_84_shift_southwest_pixels_5',
        "command": 'shift_southwest_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_84_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_84_shift_southwest_pixels_7',
        "command": 'shift_southwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_84_pause_8',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_84_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_84_shift_southwest_pixels_10',
        "command": 'shift_southwest_pixels',
        "args": [25]
    },
    {
        "identifier": 'ACTION_84_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_84_ret_12',
        "command": 'ret'
    }
]
