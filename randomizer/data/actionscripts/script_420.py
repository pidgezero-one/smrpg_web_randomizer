from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_420_jump_to_subroutine_0',
        "command": 'jump_to_subroutine',
        "args": [0x4ee7]
    },
    {
        "identifier": 'ACTION_420_jmp_1',
        "command": 'jmp',
        "args": ['ACTION_416_transfer_to_xyzf_47']
    },
    {
        "identifier": 'ACTION_420_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_420_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_420_shift_z_down_pixels_4',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_420_visibility_off_5',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_420_reset_properties_6',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_420_ret_7',
        "command": 'ret'
    }
]
