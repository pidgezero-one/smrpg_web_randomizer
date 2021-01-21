from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_63_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_63_jmp_if_var_not_equals_short_1',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 13, 'ACTION_63_sequence_looping_on_3']
    },
    {
        "identifier": 'ACTION_63_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_63_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_63_sequence_playback_on_4',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_63_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_63_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_63_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 7, 'ACTION_63_play_sound_13']
    },
    {
        "identifier": 'ACTION_63_set_700C_to_current_level_8',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_63_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 457, 'ACTION_63_play_sound_11']
    },
    {
        "identifier": 'ACTION_63_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70df, 4, 'ACTION_63_play_sound_17']
    },
    {
        "identifier": 'ACTION_63_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 4]
    },
    {
        "identifier": 'ACTION_63_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_63_shift_z_up_pixels_14']
    },
    {
        "identifier": 'ACTION_63_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._113_OPEN_CHAMBER_DOOR, 4]
    },
    {
        "identifier": 'ACTION_63_shift_z_up_pixels_14',
        "command": 'shift_z_up_pixels',
        "args": [18]
    },
    {
        "identifier": 'ACTION_63_visibility_off_15',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_63_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_63_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._052_DEEP_BOUNCE, 4]
    },
    {
        "identifier": 'ACTION_63_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_63_shift_z_up_pixels_14']
    }
]
