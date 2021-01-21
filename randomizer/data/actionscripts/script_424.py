from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_424_jump_to_subroutine_0',
        "command": 'jump_to_subroutine',
        "args": [0x4f09]
    },
    {
        "identifier": 'ACTION_424_jmp_1',
        "command": 'jmp',
        "args": ['ACTION_416_transfer_to_xyzf_47']
    },
    {
        "identifier": 'ACTION_424_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_424_shift_z_down_pixels_3',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_424_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_424_ret_5',
        "command": 'ret'
    }
]
