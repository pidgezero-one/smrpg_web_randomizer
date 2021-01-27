from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_497_clear_solidity_bits_0',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_497_floating_on_1',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_497_set_700C_to_7000_short_mem_2',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x703e]
    },
    {
        "identifier": 'ACTION_497_face_east_7C_3',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_497_sequence_playback_on_4',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_497_reset_properties_5',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_497_shadow_on_6',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_497_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_497_jump_to_height_8',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_497_shift_f_direction_pixels_9',
        "command": 'shift_f_direction_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_497_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_497_shift_f_direction_pixels_11',
        "command": 'shift_f_direction_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_497_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_497_jmp_if_mario_in_air_13',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_497_pause_12']
    },
    {
        "identifier": 'ACTION_497_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ACTION_497_fixed_f_coord_off_15',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_497_ret_16',
        "command": 'ret'
    }
]
