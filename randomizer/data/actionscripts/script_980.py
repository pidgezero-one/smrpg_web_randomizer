from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_980_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_980_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_980_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_980_transfer_xyzf_pixels_3',
        "command": 'transfer_xyzf_pixels',
        "args": [251, 254, 5, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_980_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_980_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_980_shift_z_up_pixels_6',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_980_shift_z_down_pixels_7',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_980_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_980_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_980_pause_11']
    },
    {
        "identifier": 'ACTION_980_pause_10',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_980_pause_11',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_980_jmp_if_random_above_128_12',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_979_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_980_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_980_pause_4']
    }
]
