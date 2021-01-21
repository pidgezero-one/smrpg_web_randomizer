from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_54_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_54_shift_f_direction_steps_1',
        "command": 'shift_f_direction_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_54_pause_2',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_54_turn_clockwise_45_degrees_n_times_3',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_54_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_54_set_animation_speed_0']
    }
]
