from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_509_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_509_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_509_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_pause_4',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 6]
    },
    {
        "identifier": 'ACTION_509_add_z_coord_1_step_8',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_509_set_solidity_bits_9',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_509_add_z_coord_1_step_10',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_add_z_coord_1_step_12',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_shift_z_up_pixels_14',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_shift_z_up_pixels_16',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_17',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_shift_z_up_pixels_18',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_start_loop_n_times_19',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_pause_21',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_22',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_pause_23',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_24',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_pause_25',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_end_loop_26',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_27',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_shift_z_down_pixels_28',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_shift_z_down_pixels_30',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_shift_z_down_pixels_32',
        "command": 'shift_z_down_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_33',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_dec_z_coord_1_step_34',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_509_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_36',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_dec_z_coord_1_step_37',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_509_clear_solidity_bits_38',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_509_dec_z_coord_1_step_39',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_509_set_sprite_sequence_40',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_509_pause_41',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_509_visibility_off_42',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_509_pause_43',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_509_jmp_44',
        "command": 'jmp',
        "args": ['ACTION_509_clear_solidity_bits_0']
    }
]
