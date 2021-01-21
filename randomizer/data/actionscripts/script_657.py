from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_657_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_657_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_657_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_657_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_657_shift_z_up_pixels_4',
        "command": 'shift_z_up_pixels',
        "args": [10]
    },
    {
        "identifier": 'ACTION_657_shift_z_up_pixels_5',
        "command": 'shift_z_up_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_657_shift_z_up_steps_6',
        "command": 'shift_z_up_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_657_jmp_if_random_above_128_7',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_657_pause_9']
    },
    {
        "identifier": 'ACTION_657_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_657_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_657_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_657_shift_z_down_steps_11',
        "command": 'shift_z_down_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_657_set_bit_12',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_657_dec_z_coord_1_step_13',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_657_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._073_THWOMP_STOMP, 4]
    },
    {
        "identifier": 'ACTION_657_set_bit_15',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_657_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_657_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_657_pause_18',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_657_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_657_pause_20',
        "command": 'pause',
        "args": [28]
    },
    {
        "identifier": 'ACTION_657_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_657_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_657_shadow_off_0']
    }
]
