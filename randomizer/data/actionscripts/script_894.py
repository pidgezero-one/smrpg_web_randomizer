from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_894_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_894_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[]]
    },
    {
        "identifier": 'ACTION_894_ret_2',
        "command": 'ret'
    }
]
