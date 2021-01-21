from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_854_pause_0',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_854_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_854_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_854_pause_3',
        "command": 'pause',
        "args": [62]
    },
    {
        "identifier": 'ACTION_854_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [27, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_854_ret_5',
        "command": 'ret'
    }
]
