from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_914_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [5, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_914_set_object_memory_bits_1',
        "command": 'set_object_memory_bits',
        "args": [0x0e, bits=[2, 3]]
    },
    {
        "identifier": 'ACTION_914_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [11]
    },
    {
        "identifier": 'ACTION_914_jmp_if_mario_in_air_3',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_914_ret_6']
    },
    {
        "identifier": 'ACTION_914_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_914_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_914_ret_6',
        "command": 'ret'
    }
]
