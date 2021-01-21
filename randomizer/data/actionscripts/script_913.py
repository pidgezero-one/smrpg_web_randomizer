from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_913_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_913_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_913_pause_2',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_913_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_913_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_913_floating_on_5',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_913_jump_to_height_silent_6',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_913_set_solidity_bits_7',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_913_set_vram_priority_8',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_913_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_913_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_913_set_vram_priority_8']
    }
]
