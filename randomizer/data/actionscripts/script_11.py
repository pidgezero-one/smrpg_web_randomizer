from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_11_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_11_face_south_1',
        "command": 'face_south'
    },
    {
        "identifier": 'ACTION_11_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_11_floating_off_3',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_11_clear_solidity_bits_4',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_11_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_11_run_away_shift_6',
        "command": 'run_away_shift'
    },
    {
        "identifier": 'ACTION_11_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_11_set_solidity_bits_8',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_11_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._028_PIPE_ENTRANCE, 6]
    },
    {
        "identifier": 'ACTION_11_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [30, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_11_clear_solidity_bits_11',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_11_dec_z_coord_1_step_12',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_11_reset_properties_13',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_11_ret_14',
        "command": 'ret'
    }
]
