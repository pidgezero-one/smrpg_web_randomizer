from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_247_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_247_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_247_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_247_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_247_ret_4',
        "command": 'ret'
    }
]
