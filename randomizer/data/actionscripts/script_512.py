from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_512_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_512_pause_1',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_512_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_512_pause_3',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_512_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_512_pause_5',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_512_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_512_pause_7',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_512_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_512_set_sprite_sequence_0']
    },
    {
        "identifier": 'ACTION_512_ret_9',
        "command": 'ret'
    }
]
