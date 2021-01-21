from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_430_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_430_reset_properties_1',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_430_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_430_set_object_memory_bits_3',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[2, 3]]
    },
    {
        "identifier": 'ACTION_430_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [15]
    },
    {
        "identifier": 'ACTION_430_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_430_end_loop_6',
        "command": 'end_loop'
    }
]
