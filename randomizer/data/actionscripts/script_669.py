from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_669_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_669_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_669_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_669_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_669_add_z_coord_1_step_4',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_669_shift_z_up_pixels_5',
        "command": 'shift_z_up_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_669_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_669_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_669_pause_8',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_669_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_669_dec_z_coord_1_step_10',
        "command": 'dec_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_669_clear_solidity_bits_11',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_669_shift_z_down_pixels_12',
        "command": 'shift_z_down_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_669_visibility_off_13',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_669_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_669_shadow_off_0']
    }
]
