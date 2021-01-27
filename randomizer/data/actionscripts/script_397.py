from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_397_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_397_overwrite_solidity_1',
        "command": 'overwrite_solidity',
        "args": [[]]
    },
    {
        "identifier": 'ACTION_397_shadow_off_2',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_397_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_397_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [6, 3, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_397_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_397_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._048_MINECART_START, 4]
    },
    {
        "identifier": 'ACTION_397_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_397_overwrite_solidity_8',
        "command": 'overwrite_solidity',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_397_floating_on_9',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_397_shadow_on_10',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_397_shift_southwest_steps_11',
        "command": 'shift_southwest_steps',
        "args": [18]
    },
    {
        "identifier": 'ACTION_397_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_397_shift_south_pixels_13',
        "command": 'shift_south_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_397_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [1, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_397_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 4]
    },
    {
        "identifier": 'ACTION_397_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x708d, 1]
    },
    {
        "identifier": 'ACTION_397_set_bit_17',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_397_ret_18',
        "command": 'ret'
    }
]
