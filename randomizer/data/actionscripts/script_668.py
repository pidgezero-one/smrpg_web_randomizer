from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_668_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_668_pause_1',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_668_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_668_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'ACTION_668_visibility_on_5']
    },
    {
        "identifier": 'ACTION_668_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_668_pause_2']
    },
    {
        "identifier": 'ACTION_668_visibility_on_5',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_668_set_priority_6',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_668_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_668_add_z_coord_1_step_8',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_668_shift_z_up_pixels_9',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_668_set_solidity_bits_10',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_668_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_668_pause_12',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_668_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_668_dec_z_coord_1_step_14',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_668_clear_solidity_bits_15',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_668_shift_z_down_pixels_16',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_668_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_668_jmp_if_random_above_128_18',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_668_pause_2']
    },
    {
        "identifier": 'ACTION_668_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_668_shadow_off_0']
    }
]
