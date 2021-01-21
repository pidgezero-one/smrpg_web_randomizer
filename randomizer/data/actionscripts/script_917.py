from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_917_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_917_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_917_pause_2',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_917_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_917_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_917_floating_on_5',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_917_set_solidity_bits_6',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH, _0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_917_jump_to_height_silent_7',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_917_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_917_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_917_pause_8']
    }
]
