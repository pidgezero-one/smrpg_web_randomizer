from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_355_jump_to_subroutine_0',
        "command": 'jump_to_subroutine',
        "args": [0x421b]
    },
    {
        "identifier": 'ACTION_355_walk_to_xy_coords_1',
        "command": 'walk_to_xy_coords',
        "args": [16, 24]
    },
    {
        "identifier": 'ACTION_355_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_355_set_animation_speed_10']
    },
    {
        "identifier": 'ACTION_355_shadow_off_3',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_355_face_south_4',
        "command": 'face_south'
    },
    {
        "identifier": 'ACTION_355_fixed_f_coord_on_5',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_355_floating_off_6',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_355_clear_solidity_bits_7',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_355_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_355_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_355_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_355_set_solidity_bits_11',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_355_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._028_PIPE_ENTRANCE, 6]
    },
    {
        "identifier": 'ACTION_355_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [30, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_355_clear_solidity_bits_14',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_355_dec_z_coord_1_step_15',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_355_set_solidity_bits_16',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_355_reset_properties_17',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_355_fixed_f_coord_off_18',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_355_ret_19',
        "command": 'ret'
    }
]
