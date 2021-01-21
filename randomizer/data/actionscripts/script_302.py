from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_302_pause_0',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_302_set_solidity_bits_1',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_302_set_solidity_bits_2',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_302_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_302_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._089_LIT_FUSE, 4]
    },
    {
        "identifier": 'ACTION_302_pause_5',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_302_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'ACTION_302_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_302_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_302_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_302_pause_10',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_302_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_302_clear_bit_12',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_302_pause_13',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_302_clear_solidity_bits_14',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_302_clear_solidity_bits_15',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4]]
    },
    {
        "identifier": 'ACTION_302_transfer_to_xyzf_16',
        "command": 'transfer_to_xyzf',
        "args": [4, 55, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_302_ret_17',
        "command": 'ret'
    }
]
