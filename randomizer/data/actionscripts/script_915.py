from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_915_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_915_pause_1',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_915_ret_2',
        "command": 'ret'
    }
]
