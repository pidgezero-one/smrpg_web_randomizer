from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_152_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_152_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_152_sequence_looping_off_2',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_152_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_152_ret_4',
        "command": 'ret'
    }
]
