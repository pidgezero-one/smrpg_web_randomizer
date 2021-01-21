from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_556_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_556_pause_1',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_556_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_556_pause_3',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_556_ret_4',
        "command": 'ret'
    }
]
