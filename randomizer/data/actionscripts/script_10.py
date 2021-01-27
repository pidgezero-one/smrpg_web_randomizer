from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_10_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_10_clear_solidity_bits_1',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_10_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_10_face_south_3',
        "command": 'face_south'
    },
    {
        "identifier": 'ACTION_10_fixed_f_coord_on_4',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_10_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._028_PIPE_ENTRANCE, 6]
    },
    {
        "identifier": 'ACTION_10_add_z_coord_1_step_6',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_10_set_solidity_bits_7',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
    },
    {
        "identifier": 'ACTION_10_reset_properties_8',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_10_fixed_f_coord_off_9',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_10_shadow_on_10',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_10_floating_on_11',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_10_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x707c, 0]
    },
    {
        "identifier": 'ACTION_10_ret_13',
        "command": 'ret'
    }
]
